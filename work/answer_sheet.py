import pandas as pd

# ─────────────────────────────────────────────────────────────────────────────
# TASK 1: Data Understanding & Planning
# ─────────────────────────────────────────────────────────────────────────────

print(" Task 1: Data Understanding & Planning\n")

# Load the dataset (initial look)
df_raw = pd.read_csv('student_performance.csv')

print("Dataset shape:", df_raw.shape)
print("\nColumns and initial data types:")
print(df_raw.dtypes)
print("\nFirst 5 rows (raw):")
print(df_raw.head())

print("\nExpected data types (before cleaning):")
expected_types = {
    'student_id': 'string / object',
    'age': 'integer (whole years)',
    'gender': 'categorical (Male/Female or similar)',
    'attendance': 'float or integer (likely % 0–100)',
    'assignment_score': 'numeric (float or int, likely 0–100)',
    'exam_score': 'numeric (float or int, likely 0–100)',
    'final_grade': 'categorical (A/B/C/... or letter grade)',
    'department': 'categorical (CS, IT, etc.)'
}

for col, dtype in expected_types.items():
    print(f"- {col:20} → {dtype}")

print("\nCommon errors expected in this kind of institutional dataset:")
print("• Duplicated rows (same student_id or identical records)")
print("• Numeric columns stored as strings (extra characters: %, ,, spaces)")
print("• Inconsistent category spelling / case / extra spaces")
print("• Missing values as 'N/A', '-', 'null', empty strings")
print("• Out-of-range values (age 5 or 150, attendance 150 or -10)")
print("• Age stored as float instead of int")

print("\nPlanned cleaning steps (to be executed in Task 4):")
print("1. Remove duplicates")
print("2. Replace common missing markers → NaN")
print("3. Convert score columns to numeric (coerce errors → NaN)")
print("4. Impute missing values (median for numbers, mode for categories)")
print("5. Standardize categorical columns (strip, lower, title)")
print("6. Convert age to integer + bound check")
print("7. Bound numeric columns (attendance 0–100, scores 0–100)")
print("8. Verify & save cleaned version")

# ─────────────────────────────────────────────────────────────────────────────
# TASK 2: Loading Data Using pandas
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("TASK 2: Loading Data Using pandas")
print("="*70)

# We already loaded above → here we just document it properly

df = pd.read_csv('student_performance.csv')

print("Code used to load the data:")
print("df = pd.read_csv('student_performance.csv')")
print("\nExplanation:")
print("- pd.read_csv()     : reads comma-separated values file into DataFrame")
print("- By default: header=0, infer delimiter, handle common missing values")
print("\nShape after loading:", df.shape)
print("Columns:", list(df.columns))

# ─────────────────────────────────────────────────────────────────────────────
# TASK 3: Exploring dataset issues
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("TASK 3: Exploring dataset issues")
print("="*70)

# Basic structure recap
print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)

# Missing values
print("\nMissing (NaN) counts:\n", df.isna().sum())

# Duplicates
print("\nDuplicate rows count:", df.duplicated().sum())
if df.duplicated().sum() > 0:
    print("Duplicate examples:")
    print(df[df.duplicated(keep=False)].sort_values('student_id').head(8))

# Categorical inspection
print("\nCategorical columns value counts:")
for col in ['gender', 'final_grade', 'department']:
    print(f"\n{col}:")
    print(df[col].value_counts(dropna=False))

# Numeric-as-object inspection
print("\nScore columns - non-numeric detection:")
for col in ['assignment_score', 'exam_score']:
    numeric = pd.to_numeric(df[col], errors='coerce')
    invalid = numeric.isna() & df[col].notna()
    print(f"{col:18} → {invalid.sum()} non-numeric values")
    if invalid.sum() > 0:
        print("Problematic values sample:", df[invalid][col].unique()[:10])

# Range checks
print("\nAge range check:")
print(df['age'].describe())
print("Suspicious ages:", df[(df['age'] < 16) | (df['age'] > 35)][['student_id','age']].to_dict(orient='records'))

print("\nAttendance range check:")
print(df['attendance'].describe())

# ─────────────────────────────────────────────────────────────────────────────
# TASK 4: Data preparation (cleaning)
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("TASK 4: Data Preparation - Cleaning")
print("="*70)

# 1. Remove duplicates
df = df.drop_duplicates(keep='first').reset_index(drop=True)
print("After duplicate removal → shape:", df.shape)

# 2. Replace common missing markers
missing_markers = ['-', 'N/A', 'NA', 'null', 'missing', 'None', '']
for col in df.select_dtypes('object').columns:
    df[col] = df[col].replace(missing_markers, np.nan)

# 3. Convert scores to numeric
for col in ['assignment_score', 'exam_score']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("\nNaNs after numeric conversion:")
print(df[['assignment_score','exam_score']].isna().sum())

# 4. Imputation
df['age'] = df['age'].fillna(df['age'].median())
df['attendance'] = df['attendance'].fillna(df['attendance'].median())
df['assignment_score'] = df['assignment_score'].fillna(df['assignment_score'].median())
df['exam_score'] = df['exam_score'].fillna(df['exam_score'].median())

df['gender'] = df['gender'].fillna(df['gender'].mode()[0])
df['department'] = df['department'].fillna(df['department'].mode()[0])

print("\nRemaining missing values:\n", df.isna().sum())

# 5. Standardize categories
for col in ['gender', 'department', 'final_grade']:
    df[col] = df[col].astype(str).str.strip().str.lower().str.title()

# Optional gender normalization
gender_mapping = {'M': 'Male', 'F': 'Female', 'Male': 'Male', 'Female': 'Female'}
df['gender'] = df['gender'].replace(gender_mapping)

# 6. Age → integer + simple bound
df['age'] = df['age'].round().astype('Int64')
median_age = df['age'].median()
df['age'] = np.where((df['age'] < 16) | (df['age'] > 40), median_age, df['age'])

# 7. Bound numeric columns
df['attendance'] = np.clip(df['attendance'], 0, 100)
df['assignment_score'] = np.clip(df['assignment_score'], 0, 100)
df['exam_score'] = np.clip(df['exam_score'], 0, 100)

# ─────────────────────────────────────────────────────────────────────────────
# FINAL VERIFICATION & SAVE
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "="*80)
print("FINAL CLEANED DATASET")
print("="*80)

print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print("\nBasic statistics:\n", df.describe(include='all').round(2))

print("\nFirst 6 rows of cleaned data:")
print(df.head(6))

# Save cleaned version
clean_filename = 'student_performance_cleaned.csv'
df.to_csv(clean_filename, index=False)

print(f"\nCleaned dataset saved successfully as:\n→ {clean_filename}")
print("You can download / submit this file.")
print("Cleaning pipeline complete. Good luck with your assignment!")