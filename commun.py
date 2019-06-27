# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from collections import Counter
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB 
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn import model_selection
from mlxtend.classifier import StackingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.externals.joblib import dump
from sklearn.externals.joblib import load
from sklearn.metrics import classification_report

from prepro import tokenizer
from prepro import tokenizer_snowball
from prepro import remove_ascii
from prepro import getlabel
import re
import unidecode
from nltk.stem.snowball import FrenchStemmer
from stop_words import get_stop_words

asc = False
html_m = False
special = False
double_space = False
url = False
emo = False
minuscul = False
stop_words = False
stemmer = False
cross_b = False
cross_ = False

def loadcsv(filename):  
    if '.csv' in filename:
        data = pd.read_csv(filename, encoding='latin-1')
    if '.xlsx' in filename:
        data = pd.read_excel(filename)
    return data

def loadxlsx(filename):
    data = 5
    return data

def train(data, ascp, html_mp, specialp, double_spacep, urlp, minusculp, stemmerp, cross_bp, cross_p, min_numberp, stop_wordsp, emop, split, min_number, algo):
    global asc, html_m, special, double_space, url, minuscul, stemmer, cross_b, cross_, stop_words, emo
    asc = asc
    html_m = html_mp
    special = specialp
    double_space = double_spacep
    url = urlp
    emo = emop
    minuscul = minusculp
    stop_words = stop_wordsp
    stemmer = stemmerp
    cross_b = cross_bp
    min_number = min_numberp
    cross_ = cross_p
    encoder = LabelEncoder()
   
    cleanSizeText(data, int(min_number))   
    count = data['gender'].value_counts()
    X = data['text']
    y = encoder.fit_transform(data['gender'])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=float(split), random_state=0, stratify=y)
 
    
    tfidf = TfidfVectorizer(lowercase=False,
                            tokenizer=tokenizer_snowball,
                            preprocessor=preprocessor)
    
    logisticModel = LogisticRegression(multi_class='ovr', random_state=0)
    svcModel = SVC(kernel = 'linear',probability = True, random_state=0)
    forestModel = RandomForestClassifier(n_estimators = 150, random_state=0)
    knnModel = KNeighborsClassifier(n_neighbors=150)
    nbModel = MultinomialNB()
    
    
    
    adaBmodel = AdaBoostClassifier(base_estimator=logisticModel, n_estimators=150, learning_rate=1, random_state=1)
    
    gb = GradientBoostingClassifier(n_estimators=150, 
                                    learning_rate = 0.5, random_state = 0)
    
    xgbModel = XGBClassifier(n_estimators=150, learning_rate=0.75)
    
    stacking = StackingClassifier(classifiers=[forestModel, svcModel, xgbModel, gb], 
                              meta_classifier=logisticModel)
    
    voting = VotingClassifier(estimators=[
            ('lr', logisticModel), ('rf', forestModel), ('svm', svcModel), 
            ('ada',adaBmodel), ('nb', nbModel), ('st',stacking)], voting='soft')
    
    if algo == 'lr':  
        clf = Pipeline([('vect', tfidf),('clf', logisticModel)])
    elif algo == 'svc':
        clf = Pipeline([('vect', tfidf),('clf', svcModel)])
    elif algo == 'nb':
        clf = Pipeline([('vect', tfidf),('clf', nbModel)])
    elif algo == 'rf':
        clf = Pipeline([('vect', tfidf),('clf', forestModel)])
    elif algo == 'ada':
        clf = Pipeline([('vect', tfidf),('clf', adaBmodel)])
    elif algo == 'gb':
        clf = Pipeline([('vect', tfidf),('clf', gb)])
    elif algo == 'xgb':
        clf = Pipeline([('vect', tfidf),('clf', xgbModel)])
    elif algo == 'st':
        clf = Pipeline([('vect', tfidf),('clf', stacking)])
    elif algo == 'vt':
        clf = Pipeline([('vect', tfidf),('clf', voting)])
    elif algo == 'knn':
        clf = Pipeline([('vect', tfidf),('clf', knnModel)])
    else :
        clf = Pipeline([('vect', tfidf),('clf', logisticModel)])
        
    
    
    
    
   
    if cross_b:
        scores = model_selection.cross_val_score(clf, X_train, y_train, cv=int(cross_), scoring='accuracy')
        print("Accuracy CV : ",(scores.mean()))
        acc = scores.mean()
        acc = ("{0:.2f}".format(acc))
    
    else:
        clf.fit(X_train, y_train)
        predictions = clf.predict(X_test)
        
        #filename = 'model_80.pkl'
        #dump(clf, filename) 
    
        #clf = load(filename)
    
  
        acc = accuracy_score(y_test,predictions)
       # acc =classification_report(y_test, predictions)
        acc = ("{0:.2f}".format(acc))
    return ((acc), str(count), clf)
        
def preprocessor(text):
        if html_m:
            text = re.sub('<[^>]*>', '', text)
        if emo == False:
            emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
            text = (re.sub('[\W]+', ' ', text.lower()) + ' ' + ' '.join(emoticons).replace('-', ''))
        if asc:
            text = remove_ascii(text)
            
        #text = re.sub('[^\x00-\x7F]+', ' ', text)
        #u = unicode(text, "utf-8")
        #convert utf-8 to normal text
        #text = unidecode.unidecode(u)
    
        if url:
            text = re.sub('https?:\/\/.*[\r\n]*', ' ', text)
    
        if special:
            text = re.sub('[?!+%{}:;.,"\'()\[\]_]', '', text)
    
        if double_space:
            text = re.sub('\s+', ' ', text)
        
        if minuscul:
            text = text.lower()
        
        if stop_words:
            stopwords = get_stop_words('french')
            words = text.split()
            text = ''
            for word in words:
                if not word in stopwords:
                    text = text + ' ' + word
        
        
        return text 
    

def cleanSizeText(data, min_l):
    i=0
    k=0
    l=0
    for tweet in data['text']:
        #print(tweet)
        if len(tweet.split()) > min_l :
            k = k+1
        else:
            #print(tweet)
            #data2 = data.drop(data.index[i])
            data.drop(i, inplace=True)
            #data[data.text != tweet]
            l = l+1
            print(str(l))
            
        i = i+1
   # s = k+l
    
    return data
    
