                                # EXERCISES

# Importing all libraries and modules

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Predict the price of the car based on its features. Use appropriate evaluation metrics.  
#    Dataset :  cars.csv

df = pd.read_csv("cars.csv")
X = df.drop("price", axis=1)
y = df["price"]
X = pd.get_dummies(X, drop_first=True)  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))


# 2. Create a model that can predict the profit based on its features. Use appropriate evaluation metrics.
#    The  Dataset can be downloaded from kaggle.com   
#    Dataset : 50_startups.csv
	
df = pd.read_csv("50_startups.csv")
X = df.drop("Profit", axis=1)
y = df["Profit"]
X = pd.get_dummies(X, drop_first=True)  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))


# 3. Create a model that can predict the profit based on its features. Use appropriate evaluation 
#    metrics.The  Dataset can be downloaded from kaggle.com   
#    Dataset : Salary_Data

df = pd.read_csv("Salary_Data.csv")
X = df[["YearsExperience"]]  
y = df["Salary"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))
