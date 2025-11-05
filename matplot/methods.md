# 🎨 Matplotlib Quick Reference Handbook

A concise guide to **Matplotlib**, the most widely used plotting library in Python for **data science and machine learning**.

---

## 📦 Importing and Setup

```python
import matplotlib.pyplot as plt
import numpy as np
```

---

## 🧩 Basic Plotting

```python
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 16]

plt.plot(x, y)                   # Line plot
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

### Key Functions

| Function                   | Description                   |
| -------------------------- | ----------------------------- |
| `plt.plot()`               | Create a line plot            |
| `plt.scatter()`            | Create a scatter plot         |
| `plt.bar()` / `plt.barh()` | Bar and horizontal bar charts |
| `plt.hist()`               | Histogram                     |
| `plt.boxplot()`            | Box-and-whisker plot          |
| `plt.pie()`                | Pie chart                     |
| `plt.fill_between()`       | Fill area between curves      |
| `plt.stem()`               | Stem plot for discrete data   |

---

## 🖼️ Figure & Axes Management

### Object-Oriented (Recommended)

```python
fig, ax = plt.subplots(figsize=(6,4))
ax.plot(x, y, color='green', linestyle='--', marker='o', label='Data Line')
ax.set_title('Object-Oriented Plot')
ax.set_xlabel('X Values')
ax.set_ylabel('Y Values')
ax.legend()
plt.show()
```

### Common Methods

| Method                                                   | Purpose                 |
| -------------------------------------------------------- | ----------------------- |
| `ax.plot()`                                              | Plot data on Axes       |
| `ax.set_title()` / `ax.set_xlabel()` / `ax.set_ylabel()` | Labels and titles       |
| `ax.legend()`                                            | Show legend             |
| `ax.grid(True)`                                          | Add grid                |
| `ax.set_xlim()` / `ax.set_ylim()`                        | Axis limits             |
| `ax.text()` / `ax.annotate()`                            | Add text or annotation  |
| `ax.twinx()`                                             | Create secondary Y-axis |

---

## 🎨 Styling and Customization

```python
plt.plot(x, y, color='r', linestyle='--', linewidth=2, marker='o', markersize=6)
plt.grid(True, linestyle=':', linewidth=0.5)
plt.title('Styled Plot', fontsize=14, fontweight='bold')
plt.show()
```

| Argument    | Example                         | Description    |
| ----------- | ------------------------------- | -------------- |
| `color`     | `'b'`, `'red'`, `'#33cc33'`     | Line color     |
| `linestyle` | `'--'`, `':'`, `'-.'`, `'none'` | Line style     |
| `marker`    | `'o'`, `'s'`, `'^'`, `'x'`      | Point marker   |
| `linewidth` | `2`                             | Line thickness |
| `alpha`     | `0.7`                           | Transparency   |

---

## 🧮 Subplots

```python
fig, axs = plt.subplots(2, 2, figsize=(8, 6))
axs[0, 0].plot(x, y, 'r')
axs[0, 1].bar(x, y)
axs[1, 0].scatter(x, y)
axs[1, 1].hist(y)
plt.tight_layout()
plt.show()
```

| Function               | Description                     |
| ---------------------- | ------------------------------- |
| `plt.subplot(r, c, n)` | Single subplot in grid          |
| `plt.subplots()`       | Create multiple subplots easily |
| `plt.tight_layout()`   | Adjust spacing automatically    |

---

## 🌈 Colormaps & Colorbars

```python
data = np.random.rand(10, 10)
plt.imshow(data, cmap='viridis')
plt.colorbar(label='Intensity')
plt.title('Colormap Example')
plt.show()
```

Common colormaps:
`'viridis'`, `'plasma'`, `'inferno'`, `'magma'`, `'cividis'`, `'coolwarm'`, `'gray'`

---

## 📊 Special Plots

| Plot Type   | Function                           | Use Case                                                     |
| ----------- | ---------------------------------- | ------------------------------------------------------------ |
| Heatmap     | `plt.imshow()`                     | Show matrix-like data                                        |
| Contour     | `plt.contour()` / `plt.contourf()` | 2D contour lines                                             |
| 3D Plot     | `ax.plot3D()` / `ax.scatter3D()`   | 3D visualization (`from mpl_toolkits.mplot3d import Axes3D`) |
| Time Series | `plt.plot_date()`                  | Plot datetime data                                           |
| Polar Plot  | `plt.subplot(projection='polar')`  | Circular data                                                |

---

## 💾 Saving Figures

```python
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
```

| Argument              | Description                    |
| --------------------- | ------------------------------ |
| `dpi`                 | Resolution (dots per inch)     |
| `bbox_inches='tight'` | Trim whitespace                |
| Format                | `.png`, `.jpg`, `.svg`, `.pdf` |

---

## 🧠 Pro Tips

✅ Always use **`fig, ax = plt.subplots()`** for cleaner and scalable code.
✅ Combine with **Seaborn** for statistical plots.
✅ Use `plt.style.use('seaborn-v0_8')` for modern themes.
✅ Keep plots consistent — define a custom color palette and font sizes.

---

## 🧩 Useful Links

* 📘 [Matplotlib Official Docs](https://matplotlib.org/stable/contents.html)
* 🧠 [Cheat Sheet PDF (Matplotlib)](https://matplotlib.org/cheatsheets/cheatsheets.pdf)
* 🎓 [Seaborn + Matplotlib Integration](https://seaborn.pydata.org/)

---

**Author:** Aimé Kelvin SHIMWA
**Repo:** [Data Science & ML L5](https://github.com/AimeKelvin/Data_science_and_ML_L5)
📅 *A quick visual reference for daily ML workflows.*
