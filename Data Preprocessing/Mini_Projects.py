                                   # MINI PROJECT

''' Use-Case : House Price Prediction 
Dataset : melb_data.csv  

The dataset can be downloaded from melb_data.csv|Kaggle 

Perform the following tasks:  

1.Load the data in dataframe (Pandas)  
2.Handle inappropriate data 
3.Handle the missing data       
4.Handle the categorical data '''

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

df=pd.read_csv("melb_data.csv")
print(df.info())
print(df.describe(include="all"))
df=df.drop_duplicates()
num_cols=df.select_dtypes(include=['int64','float64']).columns
cat_cols=df.select_dtypes(include=['object']).columns
num_imputer=SimpleImputer(strategy='median')
df[num_cols]=num_imputer.fit_transform(df[num_cols])
cat_imputer=SimpleImputer(strategy='most_frequent')
df[cat_cols]=cat_imputer.fit_transform(df[cat_cols])
encoder=OneHotEncoder(drop='first',sparse=False,handle_unknown='ignore')
encoded=encoder.fit_transform(df[cat_cols])
encoded_df=pd.DataFrame(encoded,columns=encoder.get_feature_names_out(cat_cols),index=df.index)
df=df.drop(columns=cat_cols).join(encoded_df)
print(df.head())
