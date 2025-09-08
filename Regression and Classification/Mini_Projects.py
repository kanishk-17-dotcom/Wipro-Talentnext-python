                               # MINI PROJECTS 

# Importing all libraries and modules

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, classification_report


""" 1.
Case : Sales Prediction 
Create a model which will predict the sales based on campaigning expenses.

Dataset : Advertising.csv
The dataset can be downloaded from  https://www.kaggle.com/datasets

Perform the following task:
•Load the data in the DataFrame
•Perform  Data Preprocessing
•Handle Categorical Data
•Perform Exploratory Data Analysis
•Build the model using Multiple Linear Regression
•Use the appropriate evaluation metrics """

df = pd.read_csv("Advertising.csv")
print(df.head())
print(df.info())
print(df.describe())
df = df.dropna()
sns.pairplot(df, x_vars=["TV","Radio","Newspaper"], y_vars="Sales", kind="scatter")
plt.show()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()
X = df[["TV","Radio","Newspaper"]]
y = df["Sales"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))
print("R2 Score:", r2_score(y_test, y_pred))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.show()


""" 2.
Use Case : Diabetes Prediction
Consider the PIMA Indians diabetes dataset. Create a Model for diabetes prediction based on the 
features mentioned in the dataset.

Dataset : PIMA Indians diabetes dataset.
The dataset can be downloaded from  https://www.kaggle.com/datasets

Perform the following tasks:
•Load the data in the DataFrame
•Perform  Data Preprocessing
•Perform Exploratory Data Analysis
•Build the model using Logistic Regression and K-Nearest Neighbour
•Use the appropriate evaluation metrics """

df = pd.read_csv("diabetes.csv")
print(df.head())
print(df.info())
print(df.describe())
df = df.dropna()
sns.countplot(x="Outcome", data=df)
plt.title("Distribution of Diabetes Outcome")
plt.show()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation")
plt.show()
X = df.drop("Outcome", axis=1)
y = df["Outcome"]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, 
                                                    test_size=0.2, random_state=42, stratify=y)
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred_log = log_reg.predict(X_test)
print("Logistic Regression Results:")
print("Accuracy:", accuracy_score(y_test, y_pred_log))
print("Precision:", precision_score(y_test, y_pred_log))
print("Recall:", recall_score(y_test, y_pred_log))
print("F1 Score:", f1_score(y_test, y_pred_log))
print(confusion_matrix(y_test, y_pred_log))
print(classification_report(y_test, y_pred_log))
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
print("KNN Results:")
print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print("Precision:", precision_score(y_test, y_pred_knn))
print("Recall:", recall_score(y_test, y_pred_knn))
print("F1 Score:", f1_score(y_test, y_pred_knn))
print(confusion_matrix(y_test, y_pred_knn))
print(classification_report(y_test, y_pred_knn))
