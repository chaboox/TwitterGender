# -*- coding: utf-8 -*-
from sklearn.externals.joblib import load

def lr_predict(tweet, algo, lg):
    if lg == 'ar':
        if algo == 'lr':  
            filename = 'lr_a.pkl'
        elif algo == 'svc':
            filename = 'svc_a.pkl'
        elif algo == 'nb':
            filename = 'nb_a.pkl'
        elif algo == 'rf':
            filename = 'rf_a.pkl'
        elif algo == 'ada':
            filename = 'ada_a.pkl'
        elif algo == 'gb':
            filename = 'gb_a.pkl'
        elif algo == 'xgb':
            filename = 'xgb_a.pkl'
        elif algo == 'st':
            filename = 'st_a.pkl'
        elif algo == 'vt':
            filename = 'vt_a.pkl'
        elif algo == 'knn':
            filename = 'knn_a.pkl'
        else :
            filename = 'lr_a.pkl'
    else:
        if algo == 'lr':  
            filename = 'lr.pkl'
        elif algo == 'svc':
            filename = 'svc.pkl'
        elif algo == 'nb':
            filename = 'nb.pkl'
        elif algo == 'rf':
            filename = 'rf.pkl'
        elif algo == 'ada':
            filename = 'ada.pkl'
        elif algo == 'gb':
            filename = 'gb.pkl'
        elif algo == 'xgb':
            filename = 'xgb.pkl'
        elif algo == 'st':
            filename = 'st.pkl'
        elif algo == 'vt':
            filename = 'vt.pkl'
        elif algo == 'knn':
            filename = 'knn.pkl'
        else :
            filename = 'lr.pkl'
        
    #filename = 'model_80.pkl'
    clf = load('models/' + filename)
    #print(clf.predict(['hey hey'])[0])
    return str(clf.predict([tweet])[0])

def lr_predict_table(tweets, algo, lg):
    if lg == 'ar':
        if algo == 'lr':  
            filename = 'lr_a.pkl'
        elif algo == 'svc':
            filename = 'svc_a.pkl'
        elif algo == 'nb':
            filename = 'nb_a.pkl'
        elif algo == 'rf':
            filename = 'rf_a.pkl'
        elif algo == 'ada':
            filename = 'ada_a.pkl'
        elif algo == 'gb':
            filename = 'gb_a.pkl'
        elif algo == 'xgb':
            filename = 'xgb_a.pkl'
        elif algo == 'st':
            filename = 'st_a.pkl'
        elif algo == 'vt':
            filename = 'vt_a.pkl'
        elif algo == 'knn':
            filename = 'knn_a.pkl'
        else :
            filename = 'lr_a.pkl'
    else:
        if algo == 'lr':  
            filename = 'lr.pkl'
        elif algo == 'svc':
            filename = 'svc.pkl'
        elif algo == 'nb':
            filename = 'nb.pkl'
        elif algo == 'rf':
            filename = 'rf.pkl'
        elif algo == 'ada':
            filename = 'ada.pkl'
        elif algo == 'gb':
            filename = 'gb.pkl'
        elif algo == 'xgb':
            filename = 'xgb.pkl'
        elif algo == 'st':
            filename = 'st.pkl'
        elif algo == 'vt':
            filename = 'vt.pkl'
        elif algo == 'knn':
            filename = 'knn.pkl'
        else :
            filename = 'lr.pkl'
    #filename = 'model_80.pkl'
    clf = load('models/' + filename)
    return (clf.predict(tweets))

def model_predict_table(modelName, tweets):
    filename = modelName
    clf = load(filename)
    return (clf.predict(tweets))

def predict_with_model(modelName, tweet):
    filename = modelName
    clf = load(filename)
    return str(clf.predict([tweet])[0])
    