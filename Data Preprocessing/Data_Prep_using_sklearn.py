                                  # EXERCISES

# 1. Perform Data Preprocessing on melb_data.csv dataset with statistical perspective. The dataset 
#    can be downloaded from https://www.kaggle.com/datasets/gunjanpathak/melb-data?resource=download

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

df=pd.read_csv("melb_data.csv")
num_cols=df.select_dtypes(include=['int64','float64']).columns
cat_cols=df.select_dtypes(include=['object']).columns
num_pipeline=Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='median')),
    ('scaler',StandardScaler())
])
cat_pipeline=Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='most_frequent')),
    ('encoder',OneHotEncoder(drop='first',handle_unknown='ignore'))
])
preprocessor=ColumnTransformer(
    transformers=[
        ('num',num_pipeline,num_cols),
        ('cat',cat_pipeline,cat_cols)
    ]
)
processed=preprocessor.fit_transform(df)
processed_df=pd.DataFrame(processed.toarray() if hasattr(processed,"toarray") else processed)
print(processed_df.head())
