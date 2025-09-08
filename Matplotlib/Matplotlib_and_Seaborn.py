                                # EXERCISES 

# DOING A COMMON IMPORT OF LIBRARIES AND PACKAGES
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


# 2. Perform Exploratory Data Analysis for the dataset  salary_data. The dataset can be downloaded 
#    from  https://www.kaggle.com/datasets

df_sal = pd.read_csv("Salary_Data.csv")
print(df_sal.head(), df_sal.info(), df_sal.describe())
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.scatterplot(x="YearsExperience", y="Salary", data=df_sal, ax=axes[0])
sns.histplot(df_sal["Salary"], kde=True, ax=axes[1])
plt.show()
plt.figure(figsize=(4, 3))
sns.heatmap(df_sal.corr(), annot=True, cmap="viridis")
plt.show()


# 3. Perform Exploratory Data Analysis for the dataset  Social Network Ads. The dataset 
#    can be downloaded from  https://www.kaggle.com/datasets

df_sna = pd.read_csv("Social_Network_Ads.csv")
print(df_sna.head(), df_sna.info(), df_sna.describe())
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.countplot(x="Gender", data=df_sna, ax=axes[0])
sns.countplot(x="Purchased", data=df_sna, ax=axes[1])
plt.show()
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.histplot(data=df_sna, x="Age", hue="Purchased", kde=True, ax=axes[0])
sns.histplot(data=df_sna, x="EstimatedSalary", hue="Purchased", kde=True, ax=axes[1])
plt.show()
plt.figure(figsize=(5, 4))
sns.heatmap(df_sna[["Age", "EstimatedSalary", "Purchased"]].corr(), annot=True, cmap="Spectral")
plt.show()
