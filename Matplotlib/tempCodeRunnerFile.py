import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")


# 1. Perform Exploratory Data Analysis for the dataset Mall_Customers. The dataset can be 
#    downloaded from  https://www.kaggle.com/datasets

df = pd.read_csv("Mall_Customers.csv")
print(df.head(), df.info(), df.describe())
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.countplot(x="Gender", data=df, ax=axes[0])
sns.histplot(df["Age"], kde=True, ax=axes[1])
sns.histplot(df["Annual Income (k$)"], kde=True, ax=axes[2])
plt.show()
plt.figure(figsize=(6, 4))
sns.histplot(df["Spending Score (1-100)"], kde=True)
plt.show()
plt.figure(figsize=(5, 4))
sns.heatmap(df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]].corr(), annot=True, cmap="coolwarm")
plt.show()
