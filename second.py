# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:15:27 2023

@author: Admin
"""
import re
sentence5="sharat twitted ,Wittnessing 70th republic day India from Rajpath,new Delhi ,Mesmorizing performance by Indian Army!"
re.sub(r'/([^\s\w]|_)+', '',sentence5).split()
###Extracting n grams
#n-gram can be extracted using three techniques
#1.Custom defined function
#2.NLTK
#3.TextBlob
###############################
#extracting n-grams using custom defined function
import re
def n_gram_extractor(input_str,n):
    tokens=re.sub(r'/([^\s\w]|_)+', '',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
        
n_gram_extractor("The cute little boy is playing with kitten",2)
n_gram_extractor("The cute little boy is playing with kitten",3)

##############################################
from nltk import ngrams
#Extraction ngrams with nltk
list(ngrams("The cute littile boy is playing with kitten".split(),2))
list(ngrams("The cute littile boy is playing with kitten".split(),3))


######################################################3
from textblob import TextBlob
blob=TextBlob("The cute littile boy is playing with kitten. ")
blob.ngrams(n=2)
blob.ngrams(n=3)
#########################################################3
###Toknization using keras
sentence5
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence5)

##############################################################
#Tokenization using TextNlon
from textblob import TextBlob
blob=TextBlob(sentence5)
blob.words
################################################################
#Tweet Tokenizer
from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentence5)
#################################################################
#MultiWord Expression
from nltk.tokenize import MWETokenizer
sentence5
mwe_tokenizer=MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentence5.split())
mwe_tokenizer.tokenize(sentence5.replace('!', ' ').split())

##################################################################3
#Regular Expression tokenizer

from nltk.tokenize import RegexpTokenizer
reg_tokenizer=RegexpTokenizer('/\w+|\$[\d\.]+|\S+')
reg_tokenizer.tokenize(sentence5)
##################################################################
#White spcae tokenizer
from nltk.tokenize import WhitespaceTokenizer
wh_tokenizer=WhitespaceTokenizer()
wh_tokenizer.tokenize(sentence5)
#################################################################
from nltk.tokenize import WordPunctTokenizer
wp_tokenizer=WordPunctTokenizer()
wp_tokenizer.tokenize(sentence5)
##################################################################
#Stemmer
#It will remove the ing,ed from thw word and give the main word
sentence6="I Love plyaing cricket player practices hard in their inning"
from nltk.stem import RegexpStemmer
regex_stemmer=RegexpStemmer('ing$')
' '.join(regex_stemmer.stem(wd) for wd in sentence6.split())
####################################################################
#Porter Stemmer
#It will remove the er from the sentence and will give the orignal word
sentence7="Before eating,it would be nice to sanitize your hands with a sanitizer"
from nltk.stem.porter import PorterStemmer
ps_stemmer=PorterStemmer()
words=sentence7.split()
" ".join([ps_stemmer.stem(wd) for wd in words])
##################################################################
#Lemmatization
#It will search orginal form of word in the dictionary
import nltk 
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
nltk.download('wordnet')
lemmatization=WordNetLemmatizer()
sentence8="Thoe codes executed today are far better than what we execute generally"
words=word_tokenize(sentence8)
" ".join([lemmatization.lemmatize(word) for word in words])
##############################################################
#Singularize and pluraalization
from textblob import TextBlob
sentence9=TextBlob("She sells seashells on the seashore")
words=sentence9.words
#We want to make word[2] that is seashells in singular form
sentence9.words[2].singularize()
#We want word 5 that is seashaore in pular form
sentence9.words[5].pluralize()
##################################################################
#Language tenasalation from spanish to english
from textblob import TextBlob
en_blob=TextBlob(u'muy bien')
en_blob.translate(from_lang='es',to='en')
#es=spanish language
#en=english lagnuage
######################################################################
#Custome stopwords removal
from nltk import word_tokenize
sentence9="She sells seashells on the seashore"
custom_stop_word_list=['she','on','the','am','is']
words=word_tokenize(sentence9)
" ".join([word for word in words if word.lower() not in custom_stop_word_list])
#Select words which are not in defined list
#######################################################################
######################################################
#############################25/11/2023
"""extracting genreal features from raw text number of words
detect presence of wh word polarity,subjectivity,
langague identification"""
#To identify the number of words
import pandas as pd
df=pd.DataFrame([['The vaccine for covid-19 will be announced on 1st Auguse'],['Do you know how much expectations the world population is having from this reaserach?'],['The risk of the virus will come to an end on 31st July']])
df.columns=['text']
df
#Now let us measure the number of wordds
from textblob import TextBlob
df['number_of_words']=df['text'].apply(lambda x:len(TextBlob(x).words))
df['number_of_words']
##############################################################(
#Detect wh words are presnt in the text or not
wh_words=set(['why','what','who','how','where','when'])
df['wh_words']=df['text'].apply(lambda x:True if len(set(TextBlob(str(x)).words).intersection (wh_words))>0 else False)
df['wh_words']
##################################################################
#Finding out the polarity of the sentence
df['polarity']=df['text'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
######################################################################
sentence10="I like this example  very much"
pol=TextBlob(sentence10).sentiment.polarity
pol
sentence10="This is fantastic example and I like it very much"
pol=TextBlob(sentence10).sentiment.polarity
pol
sentence10="This was helpful example but I would have prefer another one "
pol=TextBlob(sentence10).sentiment.polarity
pol
sentence10="THis is my personal opinion that it was  helpful example but I would prefer another one"
pol=TextBlob(sentence10).sentiment.polarity
pol
sentence10="That example was not very useful to me"
pol=TextBlob(sentence10).sentiment.polarity
pol
#####################################################################################33
#Subjectivity of the dataframe df and check whether there is 
df['subjectivity']=df['text'].apply(lambda x:TextBlob(str(x)).sentiment.subjectivity)
df['subjectivity']
#####################################################################33
#To find languge of the sentece this part of the code will get https error
df['Language']=df['text'].apply(lambda x:TextBlob(str(x)).detect_language()())
#################################################################333333
#Bag of Wrods
#This BoW converts the unstructured data to the structured form
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus=['At least seven indian pharm comapnaies are working to develoop vaccine against the corona virus.','The deadly virus that has already infected more than 14 milion globally','Bharat biotech is the among the domastic pharm firm working an the corona virus  vaccine in india']
bag_of_words=CountVectorizer()
print(bag_of_words.fit_transform(corpus).todense())
bag_of_words_df=pd.DataFrame(bag_of_words.fit_transform(corpus).todense())
#This will create dataframe
bag_of_words_df.columns=sorted(bag_of_words.vocabulary_)
bag_of_words_df.head()
#########################################################
bag_of_words_small=CountVectorizer(max_features=5)
bag_of_words_df=pd.DataFrame(bag_of_words_small.fit_transform(corpus).todense())
#This will create dataframe
bag_of_words_df.columns=sorted(bag_of_words_small.vocabulary_)
bag_of_words_df.head()
