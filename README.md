# 📊 Student Performance Data Analysis

This project demonstrates the **core steps of data analysis** using Python and NumPy on a student exam dataset.
It focuses on **data preprocessing, transformation, filtering, and basic statistical insights** to extract meaningful information from structured data.

---

## 🎯 Project Objective

The goal of this project is to:

* Understand how raw data is structured and processed
* Perform data cleaning and transformation
* Apply filtering techniques to extract insights
* Generate basic statistical summaries

This represents the **foundation of any real-world data analysis pipeline**.

---

## 📁 Dataset Description

The dataset contains marks of students across multiple subjects:

* Rows → Students
* Columns → Subjects

```python
data = np.array([
 [78, 85, 90, 88],
 [67, 72, 70, 60],
 [90, 92, 94, 96],
 [56, 65, 60, 58],
 [88, 84, 82, 86],
 [73, 75, 78, 72],
 [91, 89, 93, 90],
 [64, 68, 70, 66]
])
```

---

## 🔍 Key Data Analysis Steps

### 1. 📌 Data Understanding

* Shape of dataset (`shape`)
* Dimensions (`ndim`)

✔ Helps understand dataset structure before analysis

---

### 2. 🔄 Data Transformation

* Reshaping arrays
* Flattening data
* Changing structure for analysis

✔ Real-world data often needs restructuring before use

---

### 3. 🔁 Data Iteration

* Row-wise and element-wise traversal
* Using `np.nditer()`

✔ Useful for inspecting and validating data

---

### 4. ➕ Data Integration

* Combining datasets using:

  * `concatenate`
  * `vstack`
  * `hstack`

✔ Simulates merging datasets from multiple sources

---

### 5. ✂️ Data Segmentation

* Splitting arrays using:

  * `array_split`
  * `hsplit`

✔ Helps in dividing data for batch processing or analysis

---

### 6. 🔎 Data Exploration

* Searching values using `np.where()`

Examples:

* Find specific marks
* Identify high scorers
* Locate subject-wise conditions

✔ Helps discover patterns and anomalies

---

### 7. 📊 Data Sorting

* Sorting across rows and columns

✔ Useful for ranking and comparison

---

### 8. 🎯 Data Filtering (Core Analysis)

Filtering is a key part of data analysis.

#### Example 1: High Scores (>80)

```python
filter_arr = data > 80
filtered_data = data[filter_arr]
```

#### Example 2: Students with strong first subject (>85)

Custom filtering logic is applied to extract specific student groups.

✔ This step is used in:

* Performance analysis
* Threshold-based decision making
* Identifying top performers

---

### 9. 📈 Statistical Insights

Basic statistics are used to summarize data:

```python
# Students scoring >85 in all subjects
np.all(data > 85, axis=1)

# Maximum marks per subject
np.max(data, axis=0)

# Average marks per student
np.mean(data, axis=1)
```

✔ Helps in:

* Identifying trends
* Comparing performance
* Generating insights

---

## 📸 Sample Outputs

Add screenshots of:

* Filtering results
* Sorted data
* Statistical outputs

📁 Store them in:

```
screenshots/
```

Example:

```
screenshots/filter.png
screenshots/sort.png
screenshots/mean.png
```

---

## 🛠 Tech Stack

* Python 3.x
* NumPy

Install dependency:

```bash
pip install numpy
```

---

## 🚀 How to Run

```bash
python main.py
```

---

## 🧠 Key Learnings

* How to structure and manipulate data using NumPy
* Importance of data preprocessing in analysis
* Applying filtering techniques to extract insights
* Performing basic statistical analysis

---

## 📌 Project Scope

This project focuses on **foundational data analysis**:

* Data cleaning
* Data transformation
* Data filtering
* Basic statistical exploration

---

## 🚀 Future Improvements

To extend this into an advanced data analysis project:

* 📊 Data visualization using Matplotlib / Seaborn
* 📈 Trend analysis and comparisons
* 🏆 Ranking and performance dashboards
* 🤖 Machine learning models for prediction

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and enhance the project.

---

## 📜 License

MIT License
