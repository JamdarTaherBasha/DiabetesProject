# Diabetes Prediction using Machine Learning

This project is focused on building a machine learning model that can predict whether a person is diabetic or not based on certain medical attributes. I used the Pima Indians Diabetes dataset and applied several classification algorithms to compare their performance.

---

## 📌 Dataset

- **Source:** The dataset used is from the Pima Indians Diabetes Database, which is commonly used in binary classification problems related to diabetes.
- **Features:** The dataset contains attributes like:
  - Number of pregnancies
  - Glucose concentration
  - Blood pressure
  - Skin thickness
  - Insulin levels
  - BMI (Body Mass Index)
  - Diabetes Pedigree Function
  - Age
  - Diabetes outcome (0 or 1)

---

## 🛠 Libraries Used

- `pandas`, `numpy` – Data handling and preprocessing
- `matplotlib` – Data visualization
- `sklearn` – Machine learning models and utilities
- `pickle` – Saving models and preprocessing objects

---

## ✅ Steps Followed

### 1. Data Collection and Loading
I loaded the data from an Excel file using `pandas.read_excel()` after downloading the dataset from an online source.

### 2. Data Cleaning and Preprocessing
- Checked for null values (no NaNs but several zeroes in place of missing values).
- Removed duplicate or highly correlated columns (like `thickness`, `diabetes_orig`, and `has_diabetes`) based on correlation matrix.
- Converted boolean columns to integers for modeling.
- Replaced zero values in important features (`glucose_conc`, `insulin`, `bmi`, etc.) using mean imputation.
- Standardized the features using `StandardScaler`.

### 3. Train-Test Split
Split the dataset into training (70%) and testing (30%) sets using `train_test_split()`.

### 4. Model Training
I trained and tested the following algorithms:
- **Naive Bayes**
- **Random Forest**
- **K-Nearest Neighbors (KNN)**

Each model was evaluated using:
- Accuracy
- Confusion Matrix
- Precision, Recall, F1-Score

### 5. Model Evaluation

| Algorithm      | Train Accuracy | Test Accuracy |
|----------------|----------------|----------------|
| Naive Bayes    | ~75%           | ~73%           |
| Random Forest  | ~100% (train)  | ~75%           |
| KNN            | ~83%           | ~70%           |

**Random Forest** performed the best overall and was chosen for deployment.

---

## 🎯 Prediction Example

I tested the model on a new sample input:
```python
input_data = [2, 197, 70, 543, 30.5, 0.158, 53, 1.773]
