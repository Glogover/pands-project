# Iris Dataset Analysis

Author: **Marcin Kaminski**

## 📊 Project Overview

This project performs an exploratory data analysis (EDA) on the classic Iris dataset — one of the earliest and most widely used datasets in statistics and machine learning. It includes:

- Summary statistics.
- Visualizations (histograms, scatter plots).
- Detailed analysis by iris class.

---

## 📁 Dataset Information

- **Description:**  
  The dataset contains 150 samples of iris plants, divided into 3 classes (50 samples each):
  - Iris Setosa
  - Iris Versicolor
  - Iris Virginica

- **Attributes:**  
  Four numerical features per sample:
  - Sepal length
  - Sepal width
  - Petal length
  - Petal width

- **Predicted Attribute:**  
  Iris plant class.

- **Important Note:**  
  This dataset differs slightly from Fisher's original paper:
  - Sample 35: fourth feature should be `0.2` (Iris-setosa).
  - Sample 38: second and third features should be `3.6` and `1.4` respectively (Iris-setosa).

- **Source:**  
  [UCI Machine Learning Repository — Iris Dataset](https://archive.ics.uci.edu/dataset/53/iris)

---

## ⚙️ Scripts

### `analysis.py`

- Outputs a summary of each variable to a text file.
- Saves a histogram of each variable as PNG files.
- Creates scatter plots of each pair of variables.
- Performs additional appropriate analysis.

### `analysis.ipynb`

- General overview.
- Detailed analysis for:
  - Iris Setosa
  - Iris Versicolor
  - Iris Virginica
- Summary of findings.

---

## 📦 Used Libraries

- pandas  
- matplotlib.pyplot  
- seaborn  
- json  
- subprocess  

---

## 🔗 References

1. [Pandas read_csv](https://datascienceparichay.com/article/read-csv-files-using-pandas-with-examples/)  
2. [Pandas sample](https://www.w3schools.com/python/pandas/ref_df_sample.asp)  
3. [Pandas describe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)  
4. [Python with statement](https://www.geeksforgeeks.org/how-to-open-a-file-using-the-with-statement/)  
5. [Matplotlib figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)  
6. [Seaborn histplot](https://seaborn.pydata.org/generated/seaborn.histplot.html)  
7. [Matplotlib title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html)  
8. [Matplotlib xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html)  
9. [Matplotlib ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html)  
10. [Matplotlib grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html)  
11. [Matplotlib tight_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html)  
12. [Matplotlib savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)  
13. [Matplotlib close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html)  
14. [Pandas select_dtypes](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.select_dtypes.html)  
15. [Python enumerate](https://docs.python.org/3.12/library/functions.html#enumerate)  
16. [Seaborn scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html)  

---

## 📬 Contact

Marcin Kaminski → [marcin442228@gmail.com](mailto:marcin442228@gmail.com)

---




