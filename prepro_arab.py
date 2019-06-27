# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 19:01:23 2019

@author: achour_ar
"""

import re
import unidecode
from nltk.stem.snowball import ArabicStemmer
from stop_words import get_stop_words

stemmer = ArabicStemmer()

def preprocessor(text):
 
    # Remove HTML markup
    text = re.sub('<[^>]*>', '', text)
    # Save emoticons for later appending
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    # Remove any non-word character and append the emoticons,
    # removing the nose character for standarization. Convert to lower case
    text = (re.sub('[\W]+', ' ', text.lower()) + ' ' + ' '.join(emoticons).replace('-', ''))
    
    # Remove URLs
    text = re.sub('https?:\/\/.*[\r\n]*', ' ', text)
        

    # Remove special chars.
    text = re.sub('[?!+%{}:;.,"\'()\[\]_]', '', text)

    # Remove double spaces.
    text = re.sub('\s+', ' ', text)
    
    # Remove non-arabic words
    words = text.split()
    text = ''
    for word in words:
        search = re.search('^[a-zA-Z]+$', str(word))
        if (search == None):
            text = text + ' ' + word
            
    # Stop words
    stopwords = get_stop_words('arabic')

    words = text.split()
    text = ''
    for word in words:
        if not word in stopwords:
            text = text + ' ' + word
    
    
    return text


def tokenizer(text):
    return text.split()


def tokenizer_snowball(text):
    return [stemmer.stem(word) for word in text.split()]

def remove_ascii(text):
    # Remove non-ASCII chars.
    return re.sub('[^\x00-\x7F]+', ' ', text)

def cleanSizeText(data):
    i=0
    k=0
    l=0
    for tweet in data['text']:
        #print(tweet)
        if len(tweet.split()) > 10 :
            k = k+1
        else:
            #print(tweet)
            #data2 = data.drop(data.index[i])
            data.drop(i, inplace=True)
            #data[data.text != tweet]
            l = l+1
            print(str(l))
            
        i = i+1
    print('number of tweet > 10 :',str(k))
    print('number of tweet < 10 :',str(l))
    s = k+l
    print('sum :',str(s))
    
    return data

def dropSomeTweets(data, number):
    data.drop(data.index[[2,number+2]])     
    return data
    

def getlabel(num):
    label = ""
    if(num == 0):
        label =  "Femme"
    else:
        label = "Homme"
    
    return label

