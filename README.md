# Credit Card Fraud Detection

## 📌 Project Overview

This project aims to detect fraudulent credit card transactions using machine learning. The dataset is highly imbalanced, with fraudulent transactions representing a very small fraction of the total. To address this, the project utilizes **SMOTE (Synthetic Minority Over-sampling Technique)** for balancing the training data and compares the performance of **XGBoost** and **Random Forest** classifiers.

## 📂 Project Structure

* **`eda.ipynb`**: Notebook for Exploratory Data Analysis. It visualizes the data distribution, checks for class imbalance, and analyzes relationships between features.
* **`model.ipynb`**: The core machine learning notebook. It handles data preprocessing (scaling), resampling (SMOTE), hyperparameter tuning, model training, and performance evaluation.
* **`Model_data_creditcard.csv`**: The dataset file used for training and testing the models.

## 📊 Dataset Details

The dataset contains transactions made by credit cards in September 2013 by European cardholders.

* **Features:**
* `V1` - `V28`: Principal components obtained via PCA (for confidentiality).
* `Time`: Seconds elapsed between each transaction and the first transaction.
* `Amount`: Transaction amount.


* **Target:** `Class` (0 = Legitimate, 1 = Fraudulent).
* **Imbalance:** The dataset is heavily imbalanced, with fraud cases accounting for only **0.17%** of all transactions.

## 🛠️ Methodology

### 1. Exploratory Data Analysis (EDA)

* Visualized the count of valid vs. fraud transactions.
* Analyzed the distribution of transaction amounts for both classes.
* Investigated feature correlations.

### 2. Preprocessing

* **Feature Scaling:** Applied `StandardScaler` to normalize features (Time, Amount, and V-features).
* **Data Splitting:** Split data into training (70%) and testing (30%) sets.

### 3. Handling Imbalance

* Used **SMOTE** (Synthetic Minority Over-sampling Technique) on the training data to generate synthetic samples for the minority class (Fraud), ensuring the model learns the characteristics of fraudulent transactions effectively.

### 4. Model Training & Tuning

Two primary models were trained and tuned using a custom grid search approach:

* **XGBoost Classifier:** A gradient boosting framework known for speed and performance.
* **Random Forest Classifier:** An ensemble learning method using multiple decision trees.

Key hyperparameters tuned included `n_estimators`, `max_depth`, `learning_rate` (for XGB), and `min_samples_leaf` (for RF).

### 5. Evaluation

Models were evaluated based on **F1-Score** and **Recall** rather than just accuracy (due to class imbalance). Threshold tuning was performed using the Precision-Recall curve to find the optimal probability threshold.

## 📈 Results

| Model | Accuracy | Best F1-Score | Optimal Threshold |
| --- | --- | --- | --- |
| **XGBoost** | 99.97% | **0.8947** | 0.3189 |
| **Random Forest** | 99.97% | 0.8880 | 0.4174 |

* **XGBoost** slightly outperformed Random Forest with a higher F1-score.
* Confusion matrices showed both models effectively minimized false positives while maintaining high recall for fraud cases.

## 💻 Requirements

To run this project, you need the following Python libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost imbalanced-learn

```

* **Note:** The notebooks may reference `cuml` (RAPIDS) for GPU acceleration. If you are running on a CPU-only machine, ensure you are using the standard `scikit-learn` and `xgboost` libraries as imported in `model.ipynb`.

## 🚀 Usage

1. Ensure `Model_data_creditcard.csv` is in the same directory as the notebooks.
2. Run **`eda.ipynb`** to generate visualizations and understand the data.
3. Run **`model.ipynb`** to train the models, tune hyperparameters, and output the evaluation metrics.# Credit-Card-Fraud-Detection---ML
