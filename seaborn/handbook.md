# 🐧 Seaborn — Statistical Data Visualization (README)

This README.md is a single-file reference for **Seaborn** (v0.11+ / 0.12+). It summarizes the most important built-in functions a user should know, common methods, configuration options, and best practices for creating clear, effective statistical visualizations.

> **Audience:** data scientists, analysts, students, and engineers who use Python + pandas and want a concise reference to Seaborn's common API and best practices.

---

## 📌 Table of contents

1. What is Seaborn
2. Installation & import
3. Data expectations (pandas-friendly)
4. Figure-level vs Axes-level functions
5. Core functions (grouped by purpose)
6. Common parameters and styling
7. Color palettes & themes
8. Composability with Matplotlib
9. Best practices
10. Performance tips
11. FAQs & troubleshooting
12. Example recipes

---

## 1 — What is Seaborn

Seaborn is a high-level visualization library built on top of Matplotlib focused on statistical graphics. It simplifies common visualization tasks (distributions, categorical comparisons, relationships, regression) and integrates tightly with pandas DataFrames.

## 2 — Installation & import

```bash
pip install seaborn
```

```py
import seaborn as sns
import matplotlib.pyplot as plt
```

If you use an environment like Jupyter, add:

```py
%matplotlib inline
```

## 3 — Data expectations

* Seaborn works best with **tidy** (long) data where each row is an observation and columns are variables.
* Many functions accept NumPy arrays, but passing a `pandas.DataFrame` with named columns enables easy mapping using `x=`, `y=`, `hue=`, `col=`, `row=`.
* Handle missing values before plotting if you want consistent behavior; most functions ignore NA but can behave unexpectedly in facetting.

## 4 — Figure-level vs Axes-level functions

Seaborn is split into two categories:

**Figure-level functions** create a figure and possibly a grid of subplots. They accept `data=` and mappings and return a `FacetGrid` or `Figure`.

* `sns.relplot()`
* `sns.catplot()`
* `sns.displot()`
* `sns.pairplot()`
* `sns.jointplot()`

**Axes-level functions** draw to an existing Matplotlib axes. They return `Axes` or artists and are more flexible for composition.

* `sns.scatterplot()`, `sns.lineplot()`, `sns.boxplot()`, `sns.heatmap()`, etc.

Use figure-level to quickly explore and axes-level to fine-tune and compose plots.

## 5 — Core functions (grouped)

### A. Relational plots (relationships)

* `sns.relplot(data=..., x=..., y=..., kind='scatter'|'line', hue=..., col=..., row=...)` — figure-level wrapper for `scatterplot` and `lineplot` with facets.
* `sns.scatterplot()` — scatter plot, great with `hue`, `style`, `size` mappings.
* `sns.lineplot()` — lines connecting points; supports confidence intervals (`ci=`) and error bars.

**Useful params:** `hue`, `style`, `size`, `palette`, `alpha`, `markers`, `legend`.

### B. Distribution plots (univariate / bivariate)

* `sns.displot(data=..., x=..., kind='hist'|'kde'|'ecdf'|'histkde')` — figure-level distribution plotting with faceting.
* `sns.histplot()` — histogram; supports `bins`, `stat`, `element` (`'bars'|'step'|'poly'`), `multiple`.
* `sns.kdeplot()` — kernel density estimate; `bw_adjust`, `fill`, `clip`.
* `sns.ecdfplot()` — empirical cumulative distribution.
* `sns.rugplot()` — mark individual observations on an axis (often combined with `kdeplot`).

**Useful params:** `bins`, `stat` (`'count'|'density'|'probability'`), `common_norm`, `hue`, `multiple`.

### C. Categorical plots

* `sns.catplot(kind=...)` — figure-level wrapper for categorical plots.
  Axes-level categorical plots:
* `sns.boxplot()` — box-and-whisker plots; useful for showing distribution percentiles.
* `sns.violinplot()` — shows kernel density for each category; can be split, inner quartiles.
* `sns.stripplot()` — scatter on categorical axis (can be jittered).
* `sns.swarmplot()` — better non-overlapping scatter for small/medium datasets.
* `sns.barplot()` — bars with estimator (default `np.mean`) and CI.
* `sns.countplot()` — counts for categorical variable.
* `sns.pointplot()` — point estimates and confidence intervals (like barplot but points + line).

**Useful params:** `order`, `hue_order`, `estimator`, `ci`, `orient`, `saturation`, `dodge`, `linewidth`.

### D. Regression and statistical estimation

* `sns.regplot()` — axes-level linear regression plot with scatter + regression line and CI.
* `sns.lmplot()` — figure-level wrapper combining `regplot` with `FacetGrid`.
* `sns.residplot()` — residual plot (observed - predicted).
* `sns.polynomial_regression()` — (not in older versions) use `sns.lmplot(..., order=2)` or sklearn + manual plotting for polynomial fits.

### E. Matrix plots and heatmaps

* `sns.heatmap()` — matrix values visualized as colors; supports annotations, masks, colormaps.
* `sns.clustermap()` — hierarchical clustering + heatmap with dendrograms — good for gene expression or similarity matrices.

**Useful params:** `annot`, `fmt`, `cmap`, `center`, `vmin`, `vmax`, `mask`, `linewidths`.

### F. Multi-plot grids

* `sns.pairplot()` — scatterplots for pairwise relationships and univariate distributions on the diagonal.
* `sns.PairGrid()` — customize pairwise grids (use `.map()`, `.map_diag()`, `.map_offdiag()`).
* `sns.FacetGrid()` — manual faceting control with `.map()` or `.map_dataframe()`.

### G. Specialized plots

* `sns.jointplot()` — combined bivariate plot (scatter or KDE) with marginal distributions.
* `sns.kdeplot()` — 1D/2D KDE; `fill=True` for area shading.
* `sns.heatmap()` / `sns.clustermap()` described above.

## 6 — Common parameters & methods explained

* `data` — DataFrame or array-like. Prefer DataFrame for named mappings.
* `x`, `y`, `hue`, `row`, `col`, `size`, `style` — variable mappings, usually column names.
* `palette` — color palette name or list/dict mapping.
* `ci` — size of confidence interval to draw for estimate (e.g., `95` or `None`).
* `estimator` — function to aggregate values for categorical plots (e.g., `np.mean`, `np.median`).
* `order`, `hue_order` — explicit ordering of categories.
* `sharex`, `sharey` (FacetGrid) — whether facets share axes.
* `ax` — axes to plot onto (for axes-level functions).

## 7 — Color palettes & themes

Seaborn provides built-in themes and palettes to make plots attractive and consistent.

**Theme presets:** `sns.set_theme(style='darkgrid')`; styles: `'darkgrid'`, `'whitegrid'`, `'dark'`, `'white'`, `'ticks'`.

**Palette functions:**

* `sns.color_palette('deep')` — returns a list of colors.
* `sns.set_palette('pastel')` — set default palette globally.
* `sns.diverging_palette()`, `sns.cubehelix_palette()`, `sns.light_palette()`, `sns.dark_palette()` — create custom palettes.
* `sns.palplot()` — visualize a palette.

**Tips:**

* Use qualitative palettes for categorical data and sequential/diverging palettes for numeric scales.
* For colorblind-safe palettes, try `sns.color_palette('colorblind')`.

## 8 — Composability with Matplotlib

* Every Seaborn plot is a Matplotlib object — you can call `plt.title()`, `ax.set_xlabel()`, `ax.legend()` afterward.
* Example:

```py
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x='category', y='value', ax=ax)
ax.set_title('Category distribution')
plt.tight_layout()
```

* Use `sns.set_theme()` to set defaults; use `plt.rcParams` for low-level Matplotlib control.

## 9 — Best practices

1. **Prefer tidy data:** columns for variables, rows for observations. Use `pd.melt()` to reshape wide to long.
2. **Start with figure-level for exploration:** `relplot`, `displot`, `catplot` provide useful quick faceting.
3. **Move to axes-level for publication:** `scatterplot`, `lineplot`, `heatmap` + Matplotlib commands let you fine-tune.
4. **Annotate thoughtfully:** annotate means and sample sizes when useful. `annotate()` or `ax.text()` are helpful.
5. **Be careful with KDEs on small samples:** `kdeplot` can mislead with small n — prefer `rugplot` or show raw points.
6. **Use appropriate scales:** use `log` scales when data spans orders of magnitude (`ax.set_xscale('log')`).
7. **Show raw data when possible:** e.g., overlay `stripplot` or `swarmplot` on `boxplot` or `violinplot` for transparency.
8. **Avoid too many colors/styles:** keep legends readable and limit `hue` levels for clarity.
9. **Save high-resolution figures for publication:** `plt.savefig('fig.png', dpi=300, bbox_inches='tight')`.
10. **Document your visual encoding:** in captions or axis labels explain `hue`/`size` mappings.

## 10 — Performance tips

* **Large datasets:** plotting every point with `scatterplot` can be slow. Consider:

  * aggregation (e.g., hexbin / 2D hist with `sns.histplot(..., bins=...)`),
  * downsampling, or
  * plotting contours (`kdeplot` for density) instead of millions of points.
* **Rasterization:** for vector outputs with many points, use `ax.scatter(..., rasterized=True)` to keep file sizes reasonable.
* **Faceting large datasets:** compute aggregates per facet before plotting instead of plotting raw rows across hundreds of facets.

## 11 — FAQs & troubleshooting

**Q: My legend is duplicated / missing.**

* When plotting multiple layers, pass `legend=False` to intermediate calls and call `ax.legend()` once. For FacetGrid, use `g.add_legend()`.

**Q: How do I control figure size?**

* For axes-level: `fig, ax = plt.subplots(figsize=(w, h))`.
* For figure-level: many functions accept `height` and `aspect` (e.g., `sns.catplot(height=4, aspect=1.5)`).

**Q: My categorical order is wrong.**

* Use `order=` for x-axis categories and `hue_order=` for hue categories. Set categorical dtype with `pd.Categorical(..., categories=[...], ordered=True)`.

**Q: How to annotate counts or p-values?**

* Compute the statistics in Python (e.g., with `scipy.stats`) and annotate with `ax.text()` or `plt.annotate()`.

## 12 — Example recipes

### A. Quick exploratory plot (relationships + hue)

```py
sns.set_theme(style='whitegrid')
sns.relplot(data=df, x='sepal_length', y='sepal_width', hue='species', kind='scatter')
plt.show()
```

### B. Distribution with histogram + KDE

```py
fig, ax = plt.subplots()
sns.histplot(data=tips, x='total_bill', kde=True, bins=30, ax=ax)
ax.set(title='Total bill distribution')
```

### C. Boxplot with raw points overlay

```py
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x='category', y='value', whis=1.5)
sns.stripplot(data=df, x='category', y='value', color='black', alpha=0.3, jitter=0.15)
```

### D. Heatmap with annotation

```py
corr = df.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt='.2f', linewidths=.5, cmap='vlag', center=0)
```

### E. Pairplot for quick pairwise exploration

```py
sns.pairplot(iris, hue='species', diag_kind='kde', corner=True)
```

---

## Appendix — Short reference table

| Purpose      |   Figure-level | Axes-level                                              |
| ------------ | -------------: | ------------------------------------------------------- |
| Relational   |    `relplot()` | `scatterplot()`, `lineplot()`                           |
| Categorical  |    `catplot()` | `boxplot()`, `violinplot()`, `barplot()`, `countplot()` |
| Distribution |    `displot()` | `histplot()`, `kdeplot()`, `ecdfplot()`                 |
| Regression   |     `lmplot()` | `regplot()`, `residplot()`                              |
| Pairwise     |   `pairplot()` | `PairGrid()`                                            |
| Matrix       | `clustermap()` | `heatmap()`                                             |

---

If you'd like, I can:

* convert this README to a GitHub-flavored markdown file ready to commit, or
* produce an abbreviated one-page cheatsheet (PNG/PDF), or
* create example notebooks demonstrating each plot type with sample datasets.
