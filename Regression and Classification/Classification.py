                                # EXERCISES

# Importing all libraries and modules

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 1. Create a model that can predict the disease of cancer based on features given in the dataset. 
#    Use appropriate evaluation metrics.  
#    Dataset : cancer.csv

df = pd.read_csv("cancer.csv")
X = df.drop("diagnosis", axis=1)
y = df["diagnosis"].map({"M":1, "B":0})  # M=Malignant, B=Benign
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


# 2. Create a model that can predict that the customer has purchased item or not based on 
#    features given in the dataset. Use appropriate evaluation metrics.  
#    Dataset : Social_Ntetwork_Ads.csv

df = pd.read_csv("Social_Network_Ads.csv")
X = df.drop("Purchased", axis=1)  
y = df["Purchased"]
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))