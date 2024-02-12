
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:46:08 2023

@author: Admin
"""

import gensim
import pandas as pd
df=pd.read_json("D:/Data Science/6-Datasets/reviews_Cell_Phones_and_Accessories_5.json/Cell_Phones_and_Accessories_5.json",lines=True)
df
df.shape
#Simple preprocessing and tokenization
review_text=df.reviewText.apply(gensim.utils.simple_preprocess)
review_text
#Let us check first word of each review
review_text.loc[0]
#Let us chech first row of the dataframe
df.reviewText.loc[0]
#Traninig the word to vec model
model=gensim.models.Word2Vec(
    window=10,
    min_count=2,
    workers=4,)
'''
Where window is the how many words you are going to consider as sliding 
window you can choose any count min_count-there are must min 2 words 
in each sentence 
workers-no of threads
'''

#Build vocabulory
model.build_vocab(review_text,progress_per=1000)
#Progress_per:After 1000 words it shown progress
#Train the word2vec model
#It will take some time
model.train(review_text,total_examples=model.corpus_count,epochs=model.epochs)
#save the model
model.save("D:/Data Science/9-NLP/word2vec-amazon-cell-accessories-reviews-short.model")
#Finding simmilar words and similarity between words
model.wv.most_similar("bad")
model.wv.similarity(w1="cheap", w2="inexpensive")
model.wv.similarity(w1="great", w2="good")

