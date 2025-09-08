                                # MINI PROJECT


""" Use Case: Perform the Outlier detection for the given dataset.
              i.e.dataset Example Dataset : datasetExample.csv

Perform the following task :
•Load the data in the DataFrame.
•Detectionof  Outliers """

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("datasetExample.csv")
print(df.describe())
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR)))
print("Outliers detected:\n", outliers.sum())
plt.figure(figsize=(12,6))
sns.boxplot(data=df)
plt.show()
