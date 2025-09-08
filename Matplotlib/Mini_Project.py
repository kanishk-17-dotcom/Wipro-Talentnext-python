                                     # MINI PROJECTS

''' Use Case : Diabetes Prediction Perform Exploratory Data Analysis for the Diabetes Dataset.
    Dataset : Diabetes.csvT
    he dataset can be downloaded from  https://www.kaggle.com/datasets
    
    Perform the following tasks :
    
    1.Load the data in the DataFrame
    2.Data Pre-processing
    3.Handle the Categorical Data
    4.Perform Uni-variate Analysis 
    5.Perform Bi-variate Analysis '''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
df = pd.read_csv("Diabetes.csv") 
print(df.head())
print(df.info())
print(df.describe())
print("Missing values:\n", df.isnull().sum())
cols_with_zero = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
df[cols_with_zero] = df[cols_with_zero].replace(0, np.nan)
for col in cols_with_zero:
    df[col].fillna(df[col].median(), inplace=True)
print("After preprocessing:\n", df.info())
print(df["Outcome"].value_counts())
df.hist(figsize=(12, 10), bins=20, edgecolor="black")
plt.suptitle("Histograms of Features")
plt.show()
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, orient="h")
plt.title("Boxplots of Features")
plt.show()
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Glucose", hue="Outcome", kde=True, bins=30)
plt.title("Glucose Distribution by Outcome")
plt.show()
plt.figure(figsize=(6, 4))
sns.boxplot(x="Outcome", y="BMI", data=df)
plt.title("BMI vs Outcome")
plt.show()
sns.pairplot(df[["Age", "Glucose", "BMI", "Outcome"]], hue="Outcome", diag_kind="kde")
plt.show()
