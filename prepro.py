# -*- coding: utf-8 -*-
"""
Created on Sat May 11 13:27:32 2019

@author: achour_ar
"""

import re
import unidecode
from stop_words import get_stop_words
from nltk.stem.snowball import FrenchStemmer
stemmer = FrenchStemmer()

def preprocessor(text):
    
    # Remove HTML markup
    text = re.sub('<[^>]*>', '', text)
    # Save emoticons for later appending
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    # Remove any non-word character and append the emoticons,
    # removing the nose character for standarization. Convert to lower case
    text = (re.sub('[\W]+', ' ', text.lower()) + ' ' + ' '.join(emoticons).replace('-', ''))
    
    # Remove non-ASCII chars.
    text = remove_ascii(text)
    #text = re.sub('[^\x00-\x7F]+', ' ', text)
    #u = unicode(text, "utf-8")
    #convert utf-8 to normal text
    #text = unidecode.unidecode(u)

    # Remove URLs
    text = re.sub('https?:\/\/.*[\r\n]*', ' ', text)

    # Remove special chars.
    text = re.sub('[?!+%{}:;.,"\'()\[\]_]', '', text)

    # Remove double spaces.
    text = re.sub('\s+', ' ', text)
    
    #To lower case
    text = text.lower()
    
    # Stop words
    stopwords = get_stop_words('french')

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
    """text = re.sub('[^\x00-\x7F]+', ' ', text)
    u = unicode(text, "utf-8")
    #convert utf-8 to normal text
    return unidecode.unidecode(u)"""
    return re.sub('[^\x00-\x7F]+', ' ', text)

def getlabel(num):
    label = ""
    if(num == 0):
        label =  "Femme"
    else:
        label = "Homme"
    
    return label
    
    


