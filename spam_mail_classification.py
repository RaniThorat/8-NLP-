# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:07:05 2023

@author: Admin
"""

import pandas as pd
import numpy as np
#Read the csv
df=pd.read_csv("C:/datasets/spam.csv")
#Check the first 10 records
df.head(10)
#Total no of spam and ham
df.Category.value_counts()   #ham     4825
                             #spam     747
#Create one more column comprises 0 and 1
#Name of column is spam
df['spam']=df['Category'].apply(lambda x: 1 if x=='spam' else 0)
df.shape #5572,3
'''#################################################################'''
#Train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.Message, df.spam, test_size=0.2)

#Let us check the shape of X_train data and X_test data
X_train.shape   #(4457,)
X_test.shape    #(1115,)

#Let us check the type of X_train and X_test
type(X_train)
type(X_test)
# pandas.core.series.Series
'''#######################################################################'''

#Create bag of words representation using ountVectorize
from sklearn.feature_extraction.text import CountVectorizer
v = CountVectorizer()
X_train_cv=v.fit_transform(X_train.values)
X_train_cv

#After creation of BoW let us check shape
X_train_cv.shape
#(4457, 7796)

'''###############################################################'''
#Train the naive bayes model
from sklearn.naive_bayes import MultinomialNB
#Initialize the model
model=MultinomialNB()
#Train the model
model.fit(X_train_cv,y_train)

'''#################################################################'''
#Create a bag of words representationn using Countvectorizer of X_test
X_test_cv=v.transform(X_test)

'''################################################################'''
from sklearn.metrics import classification_report
y_pred=model.predict(X_test_cv)
print(classification_report(y_test, y_pred))
'''
precision    recall  f1-score   support

           0       0.99      0.99      0.99       964
           1       0.96      0.93      0.94       151

    accuracy                           0.98      1115
   macro avg       0.97      0.96      0.97      1115
weighted avg       0.98      0.98      0.98      1115
'''