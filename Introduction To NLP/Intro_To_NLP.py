                              # EXERCISES

# 1. Perform Text Preprocessing on SMS Spam Collection Dataset. 
#    The dataset can be downloaded from  https://www.kaggle.com/datasets

import pandas as pd
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')
stop_words=set(stopwords.words('english'))
ps=PorterStemmer()
df=pd.read_csv("spam.csv",encoding='latin-1')
df=df[['v1','v2']]
df.columns=['label','message']
def preprocess_text(text):
    text=text.lower()
    text=re.sub(r'\d+','',text)
    text=text.translate(str.maketrans('','',string.punctuation))
    tokens=text.split()
    tokens=[word for word in tokens if word not in stop_words]
    tokens=[ps.stem(word) for word in tokens]
    return " ".join(tokens)
df['clean_message']=df['message'].apply(preprocess_text)
print(df.head())
