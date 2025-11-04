
1. Data Loading & Saving
pd.read_csv()      # load CSV files
pd.read_excel()    # load Excel files
pd.read_json()     # load JSON files
DataFrame.to_csv() # save to CSV

2. Exploration & Inspection
df.head()        # first few rows
df.tail()        # last few rows
df.info()        # data types + missing info
df.shape         # number of rows/columns
df.describe()    # summary statistics
df.columns       # column names
df.dtypes        # data types per column
df.isnull().sum()# missing values per column
df.nunique()     # number of unique values per column

3. Cleaning & Preprocessing
df.dropna()          # remove missing rows
df.fillna(value)     # fill missing values
df.drop(columns=...) # remove columns
df.rename(columns=...) # rename columns
df.replace(old, new) # replace values
df.astype('float')   # convert data type
df.duplicated()      # check duplicates
df.drop_duplicates() # remove duplicates

4. Selecting & Filtering
df['column']                # select a column
df[['col1', 'col2']]        # select multiple columns
df.iloc[5]                  # row by position
df.loc[10]                  # row by label/index
df.loc[df['age'] > 30]      # filter rows by condition
df.query("age > 30 & city == 'Berlin'")  # SQL-style filtering

5. Aggregation & Summaries
df['salary'].mean()
df.groupby('department')['salary'].mean()
df.value_counts('city')
df.sort_values(by='age', ascending=False)
df.corr()   # correlation matrix

6. Feature Engineering
pd.get_dummies(df['gender'])           # one-hot encoding
df['log_income'] = np.log(df['income']) # transform values
df['age_bin'] = pd.cut(df['age'], bins=[0,18,35,60,100])
df['city_encoded'] = LabelEncoder().fit_transform(df['city'])

7. Merging, Joining, and Reshaping
pd.concat([df1, df2])                # stack DataFrames
pd.merge(df1, df2, on='id')          # SQL-style join
df.pivot(index='id', columns='year', values='sales') # reshape
df.melt(id_vars=['id'], var_name='year', value_name='sales') # reverse pivot

8. Visualization (exploratory)
import matplotlib.pyplot as plt
import seaborn as sns

df['age'].hist()
sns.boxplot(x='gender', y='salary', data=df)
sns.heatmap(df.corr(), annot=True)

9. Machine Learning Integration
from sklearn.model_selection import train_test_split

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
