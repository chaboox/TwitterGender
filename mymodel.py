# -*- coding: utf-8 -*-
from sklearn.externals.joblib import load

def lr_predict(tweet):
    filename = 'model_80.pkl'
    clf = load(filename)
    #print(clf.predict(['hey hey'])[0])
    return str(clf.predict([tweet])[0])

def lr_predict_table(tweets):
    filename = 'model_80.pkl'
    clf = load(filename)
    return (clf.predict(tweets))