# -*- coding: utf-8 -*-
"""
Created on Sat May 11 13:03:21 2019

@author: achour_ar
"""

# Import libraries

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

from prepro import preprocessor
from prepro import tokenizer
from prepro import tokenizer_snowball
from prepro import remove_ascii
from prepro import getlabel


# Load csv file
data = pd.read_csv('79_.csv', encoding='latin-1')

# Just see the counts
data['gender'].value_counts()

data = data[data['text'].notnull()]

data['gender'].value_counts()


encoder = LabelEncoder()
y = encoder.fit_transform(data['gender'])

# split the dataset in train and test
X = data['text']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)
#In the code line above, stratify will create a train set with the same class balance than the original set

X_train.head()

tfidf = TfidfVectorizer(lowercase=False,
                        tokenizer=tokenizer_snowball,
                        preprocessor=preprocessor)

logisticModel = LogisticRegression(multi_class='ovr', random_state=0)
svcModel = SVC(kernel = 'linear',probability = True, random_state=0)
forestModel = RandomForestClassifier(n_estimators = 150, random_state=0)
knnModel = KNeighborsClassifier(n_neighbors=150)
nbModel = MultinomialNB()



# Using Probabilities as Meta-Features
stacking_prob = StackingClassifier(classifiers=[forestModel, svcModel, logisticModel],
                                            use_probas=True,
                                            average_probas=False,
                                            meta_classifier=logisticModel)

adaBmodel = AdaBoostClassifier(base_estimator=logisticModel, n_estimators=150, learning_rate=1, random_state=1)

gb = GradientBoostingClassifier(n_estimators=150, 
                                learning_rate = 0.5, random_state = 0)

xgbModel = XGBClassifier(n_estimators=150, learning_rate=0.75)

stacking = StackingClassifier(classifiers=[forestModel, svcModel, xgbModel, gb], 
                          meta_classifier=logisticModel)

voting = VotingClassifier(estimators=[
        ('lr', logisticModel), ('rf', forestModel), ('svm', svcModel), 
        ('ada',adaBmodel), ('nb', nbModel), ('st',stacking)], voting='soft')

    
clf = Pipeline([('vect', tfidf),
                ('clf', voting)])



print('3-fold cross validation:\n')

scores = model_selection.cross_val_score(clf, X_train, y_train, cv=10, scoring='accuracy')
print("Accuracy CV : ",(scores.mean()))


#clf.fit(X_train, y_train)
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

print(tfidf.norm)

filename = 'model_80.pkl'
dump(clf, filename) 

clf = load(filename)

x_new = ["hey les filles je viens d'acheter une nouvelle boite de maquillage j'ai super haaate",
         "Les quatre beaux gosses (au physique de podcast) sont de retour pour parler d'engagement et du FoMO en amour.",
         "j'en ai marre tous les personnages préféré de mes séries meurent surtout lui :(((( ",
         "Neymar c’est le football samba marié au football favelas.",
         "Les deux otages libérés, seraient-ils même des agents français, que leur accueil par le président Macron et le gouvernement français est une insulte à la dignité de la France et au sacrifice de nos « bérets verts »."]
y_new = clf.predict(x_new)

for i in range(len(x_new)):
	print("\n\n\nTweet = %s || Predicted = %s \n\n" % (x_new[i], getlabel(y_new[i])))
    
    



acc = accuracy_score(y_test,predictions)
print('Accuracy:', acc)