                                   # EXERCISES 

# 1. Perform Data Preprocessing on melb_data.csv dataset with statistical perspective. The dataset 
#    can be downloaded from https://www.kaggle.com/datasets/gunjanpathak/melb-data?resource=download

import pandas as pd

df=pd.read_csv("melb_data.csv")
print(df.info())
print(df.describe(include="all"))
missing=df.isnull().sum()
print("Missing Values:\n",missing)
df=df.dropna(axis=0,subset=['Price'])
df=df.fillna(df.median(numeric_only=True))
num_cols=df.select_dtypes(include=['int64','float64']).columns
for col in num_cols:
    q1=df[col].quantile(0.25)
    q3=df[col].quantile(0.75)
    iqr=q3-q1
    lower=q1-1.5*iqr
    upper=q3+1.5*iqr
    df[col]=df[col].clip(lower,upper)
df=pd.get_dummies(df,drop_first=True)
print("Processed Data:\n",df.head())
