                                         # MINI PROJECTS

""" 1.
Use Case: Rating Prediction
Create a model that will predict the rating based on the feedback of the customer.

Feature: Text

Label: Stars

Dataset: yelp.csv
The dataset can be downloaded from https://www.kaggle.com/datasets """

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

df=pd.read_csv("yelp.csv")
X=df['text']
y=df['stars']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
tfidf=TfidfVectorizer(stop_words='english',max_features=5000)
X_train_tfidf=tfidf.fit_transform(X_train)
X_test_tfidf=tfidf.transform(X_test)
model=LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf,y_train)
y_pred=model.predict(X_test_tfidf)
print("Accuracy:",accuracy_score(y_test,y_pred))
print("\nClassification Report:\n",classification_report(y_test,y_pred))
