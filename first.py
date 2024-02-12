# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 20:27:59 2023

@author: Admin
"""

##################Text mining################
sentence="we are Learning TextMining from Sanjivani AI"
#if we want to a position of learning
sentence.index("Learning")
#It will show learning is at position 7
#This is going to show character position from 0 including
###############################################
#We want to know position of textmining word
sentence.split().index("TextMining")
#It will split the words in list and count the position
#if you want to see list select sentence.split() and
#it will show at 3
#####################################################
#Suppose we want print any word in reverse order
sentence.split()[2][::-1]
#[start:end end:-1(start)] will start from -1,-2,-3 till the end
#learnng will be printed as gninraeL
#################################################

#suppose want to print first and last word of the sentences
words=sentence.split()
first_word=words[0]
first_word
last_word=words[-1]
last_word
#now we want to concate the first and last word
concate_word=first_word+" "+last_word
concate_word   #concate_word: 'we AI'
#######################################################

#we want to print even word from sentences
sentence.split()[::-2]
[words[i] for i in range(len(words)) if i %2==0]
#Output-['we', 'Learning', 'from', 'AI']

################################################
#sentence
#nowwewant to display only AI
sentence[-3:]
#it will start from -3,-2,-1 i.e AI
###############################################
#Suppose we want to display entire sentence in reverse order
sentence[::-1]
#IA inavijnas morf gniniMtxet era ew
###############################################
#uppose we want to select each word and print in reversed order
words
print(" ".join(word[::-1]for word in words))
#output-ew era gninraeL gniniMtxeT morf inavijnaS IA

###################################################
#Tokenization
import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize("I am reading NLP Fundamentls")
print(words)
#########################################################
#Parts of speech taging
nltk.download("averaged_perceptron_tagger")
nltk.pos_tag(words)

######################################################
#Stops words from nltk library
from nltk.corpus import stopwords
stop_words=stopwords.words('English')
#You can verify 179 stop words in variable explore
print(stop_words)
sentence1="I am learning NLP:It is one of the most popular library in python"

#First we will toknize the sentecse
sentence_words=word_tokenize(sentence1)
print(sentence_words)

#Now let us filter the senteces1 using stop words
sentence_no_stops=" ".join([words for words in sentence_words if words not in sentence_words])
print(sentence_no_stops)
sentence1

#You can notice that am,is,of,the,most,popular,in are missing
##################################################
#Suppose we want to replace words in strinf
sentence2="I visited MY from IND on 14-02019"
normalized_sentence=sentence2.replace("MY", "Malysia").replace("IND","Inida")
normalized_sentence=normalized_sentence.replace("-19", "-2020")
print(normalized_sentence)



###################################################
#For autocorrect
#Suppose we want to autocrrection in the sentecs
from autocorrect import Speller
#Declare the function speller define for english
spell=Speller(lang='en')
spell('sentecse')
######################################################
#Suppose we wnat to correct whole sentence
sentence3="Ntural language proceesing deals with the aart of extracting sentiiments"
sentence3=word_tokenize(sentence3)
#Let us first toknize these sentence
corrected_sentence=" ".join([spell(word) for word in sentence3])
print(corrected_sentence)


###########################################################
#Stemming
#22-11-23
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("Programming")
stemmer.stem("Programed")
stemmer.stem("Jumping")
stemmer.stem("Jumped")
#########################################################
#Lematizer
#lematizer looks into the dictiorny words
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("Programed")
lemmatizer.lemmatize("Program")
lemmatizer.lemmatize("Batting")
lemmatizer.lemmatize("amazing")




######################################################
#chunking (shallow parsing) identiftying named entities
import nltk
nltk.download('punkt')
from nltk import word_tokenize
nltk.download("maxent_ne_chunker")
nltk.download('averaged_perceptron_tagger')
nltk.download('words')
sentence4 = "we are laerning NLP in pytohn by sanjivani AI "
#First we will tokine
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]



###############################################################
#Sentence toknization
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("We are Learning NLP in python. Deliver by SanjivaniAI. Do you know where it is located?  It is in Kopargaon ")
sent

#######################################################3
#Sense ambiguity
from nltk.wsd import lesk
sent1="keep your saving in the bank"
print(lesk(word_tokenize(sent1),'bank'))
##
sent2="It is so risky to drive over the banks of the river"
print(lesk(word_tokenize(sent2),'bank'))
##
########
"""

a slop in thr turn of a road or tack;
the outside is higher than the inside in order to reduce the 

"Bank" as multiple meaning,If you want to find exact meaning
execute the following code
The defination for the "bank" can be seen there
"""
from nltk.corpus import wordnet as wn
for ss in wn.synset('bank'):print(ss,ss.defination())