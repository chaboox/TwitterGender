#!/usr/bin/env python
from flask import Flask, render_template, request, jsonify, flash, redirect
from flask_bootstrap import Bootstrap
from models import QuizForm, BotForm, unique_f, Dataset
from mymodel import lr_predict, lr_predict_table, predict_with_model, model_predict_table
import sys
import csv
from twitter import getTweets, getTweets2
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import os
from tkinter import filedialog
from tkinter import *
from tkinter import filedialog as fd
import pandas as pd
#import magic
import urllib.request
from tkinter.filedialog import asksaveasfilename
from werkzeug.utils import secure_filename
from commun import loadcsv, train
import xlsxwriter
from sklearn.externals.joblib import dump
from sklearn.externals.joblib import load
import json
import numpy as np
class Config(object):
    SECRET_KEY = '78w0o5tuuGex5Ktk8VvVDF9Pw3jv1MVE'
lastModel = None
application = Flask(__name__)
application.config.from_object(Config)

Bootstrap(application)

@application.route('/home', methods=['GET', 'POST'])
def home():
    print(request.method)
    return render_template('index.html')
    

@application.route('/', methods=['GET', 'POST'])
def take_test():
    print(request.method)
    form = unique_f(request.form)
    if not form.validate_on_submit():
        return render_template('unique_tweet.html', form=form)
    if request.method == 'POST':
        #return 'Submitted!'
        render_template('result.html', form=form)
        
@application.route('/unique', methods=['GET', 'POST'])
def unique():
    print(request.method)
    form = unique_f(request.form)
    if not form.validate_on_submit():
        return render_template('unique_tweet.html', form=form)
    if request.method == 'POST':
        #return 'Submitted!'
        render_template('unique_result.html', form=form)

@application.route('/bot/', methods=['GET', 'POST'])
def bot():
    print(request.method)
    form = BotForm(request.form)
    if not form.validate_on_submit():
        return render_template('bot.html', form=form)
    if request.method == 'POST':
        #return 'Submitted!'
        render_template('botresult.html', form=form)

@application.route('/unique_result', methods=['GET', 'POST'])
def result():
    print(request.method)
    
    form = unique_f(request.form)
   
    #form.tweet. = 'ada'
    if request.method == 'POST':
        if 'file' not in request.files:
            if lr_predict(request.form['tweet'], request.form['algo'], request.form['language']) == '1':
                se = 'Homme'
            else:
                se = 'Femme'
        else:
            file = request.files['file']
            if file.filename == '':
                if lr_predict(request.form['tweet'], request.form['algo'], request.form['language']) == '1':
                    se = 'Homme'
                else:
                    se = 'Femme'
            elif file and allowed_file(file.filename):
                 if predict_with_model(file.filename, request.form['tweet']) == '1':
                     se = 'Homme'
                 else:
                     se = 'Femme'
            elif lr_predict(request.form['tweet'], request.form['algo'], request.form['language']) == '1':
                 se = 'Homme'
            else:
                se = 'Femme'
        return render_template('unique_result.html', form=form, gender = se)
     
@application.route('/dataset', methods=['GET', 'POST'])
def dataset():
    print(request.method)
    form = Dataset(request.form)
    #root = Tk()
    #root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    #name = asksaveasfilename()
    #with open(name + '.csv', 'w', newline='') as csvfile:
     #   create = csv.writer(csvfile)
     #  create.writerow(["adam","deboosere"])
    
    if not form.validate_on_submit():
        return render_template('dataset.html', form=form)
    if request.method == 'POST':
        #return 'Submitted!'
        render_template('dataset.html', form=form)


@application.route('/datasetresult', methods=['GET', 'POST'])
def datasetr():
    print(request.method)
    
    form = Dataset(request.form)
    nameMale = request.form["manname"]
    femalName = request.form["womenname"]
    language = request.form["language"]
    time = request.form["time"]
    min_tweet = request.form["min_number"] 
    (tweets, y ) = getTweets2(int(time), nameMale, femalName, language , int(min_tweet))
   # tweets = ["Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies"]
    #form.tweet. = 'ada'
    #y = ["Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies"]
    y2 = np.array(y)    
    f = np.count_nonzero(y2 == 0)
    h = np.count_nonzero(y2 == 1)
    detail = [len(y), f, h]  
    #flash(str(request.form))
    if request.method == 'POST':
         return render_template('datasetresult.html', form=form, tweets=tweets, detail=detail)
     
@application.route('/savecsv', methods=['GET', 'POST'])
def savecsv():
    print(request.method)
    
    form = Dataset(request.form)
    
    if 'tweets' in request.form:
        tweets = request.form['tweets']
        tweetsR = eval(tweets)
        #return str(tweetsR[0])
        #name = asksaveasfilename()
        
        if request.form['typef'] == 'json':
            root = Tk()
            root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Destination du Json",filetypes = (("JSON","*.json"),("all files","*.*")))
    #root.mainloop()
            root.destroy()
            with open(root.filename + '.json', 'w') as out_f:
                json.dump(tweetsR, out_f)
            out_f.close()
        else:
            root = Tk()
            root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Destination du dataset",filetypes = (("xlsx","*.xlsx"),("all files","*.*")))
    #root.mainloop()
            root.destroy()
            workbook = xlsxwriter.Workbook(root.filename + '.xlsx') 
            worksheet = workbook.add_worksheet() 
    
            rowEx = 1
            worksheet.write(0, 0, 'text')
            worksheet.write(0, 1, 'gender')
            for tweet in tweetsR:            
                worksheet.write(rowEx, 0, tweet[0])
                worksheet.write(rowEx, 1, tweet[1])
                rowEx += 1
      
          
            workbook.close() 
        #with open(name + '.csv', 'w', newline='') as csvfile:
         #   create = csv.writer(csvfile)
          #  create.writerow(tweets)
   # tweets = ["Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies"]
    #form.tweet. = 'ada'
    #y = ["Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies", "Bonjour la famillle ca va !?", "Adaaam ca fait una bail", "oh la la les homme tous les meme", "Bonjouuuuuuuuuuuuuuuuuuuur mes amies"]
    
    #flash(str(request.form))
    if request.method == 'POST':
         return render_template('datasetresult.html', form=form, tweets=tweetsR)
        
@application.route('/resultbot', methods=['GET', 'POST'])
def resultbot():
    print(request.method)
    form = BotForm(request.form)
    (tweets, y) = getTweets(int(request.form['time']))
    #acc = accuracy_score(lr_predict_table(tweets),y)
    if 'file' not in request.files:
            yp = lr_predict_table(tweets, request.form['algo'], request.form['language'])
    else:
        file = request.files['file']
        if file.filename == '':
            yp = lr_predict_table(tweets, request.form['algo'], request.form['language'])
        elif file and allowed_file(file.filename):
            yp =model_predict_table(tweets)
        else:
            yp = lr_predict_table(tweets, request.form['algo'], request.form['language'])
    #yp = lr_predict_table(tweets)
    i=0
    right_prediction = 0
    array = []
    for p in y:
        if str(p) == str(yp[i]):
            right_prediction = right_prediction + 1
        else:
            array.append( [str(p) ,str(yp[i])])
        i= i + 1
    precision = (right_prediction/len(y))
    precision = ("{0:.2f}".format(precision))
    #return str(type(y)) + str(type(yp))
    #return str(right_prediction/len(y)) + str(yp) + str(y) + str(right_prediction) + str(len(y)) + str(array)  + str(yp[0])
    return render_template('botresult.html', form=form, precision= precision )
     
    #if not form.validate_on_submit():
      #  return render_template('result.html', form=form)
   # if request.method == 'POST':
       # return 'Submitted!'
       # render_template('result.html', form=form)
       
       


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    

@application.route('/apprentissage')
def upload_form():
    form=QuizForm(request.form)
    return render_template('apprentissage.html',form=form)

@application.route('/savemodel')
def savemodel():
    #
    #root.
    
#    name = asksaveasfilename()
    root = Tk()
    root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Destination du modèle",filetypes = (("PKL","*.pkl"),("all files","*.*")))
    #root.mainloop()
    root.destroy()
    print (root.filename)   
    
    #filename = 'trained_model_image.pkl'
    #dump(lastModel, name + '.pkl') 
    dump(lastModel,root.filename + '.pkl') 
    form=QuizForm(request.form)
    return render_template('apprentissage.html',form=form)

@application.route('/apprentissage', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            form = QuizForm(request.form)
            filename = secure_filename(file.filename)
            file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
            data=loadcsv('D:/uploads/' + filename)
            #count = data['gender'].value_counts()
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
            min_number = request.form['min_number']
            algo = request.form['algo']
            split = request.form['split']
            cross_ = False
            if 'asc' in request.form:
                asc = True
            if 'html_m' in request.form:
                html_m = True
            if 'special' in request.form:
                special = True
            if 'double_space' in request.form:
                double_space = True
            if 'url' in request.form:
                url = True
            if 'minuscul' in request.form:
                minuscul = True
            if 'stop_words' in request.form:
                stop_words = True
            if 'stemmer' in request.form:
                stemmer = True
            if 'cross_b' in request.form:
                cross_b = True
            if 'cross_' in request.form:
                cross_ = request.form['cross_']
            if 'emo' in request.form:
                emo = True
            (prec, count, model) =train(data, asc, html_m, special, double_space, url, minuscul, stemmer, cross_b, cross_, min_number, stop_words, emo, split, min_number, algo)
            flash( count)
            global lastModel 
            lastModel = model
            precision = str(prec)
            return render_template('apprentissageresult.html', form=form, precision = precision)
        else:
            flash('Allowed file types are csv and xlsx')
            return redirect(request.url)


if __name__ == '__main__':
           
    ALLOWED_EXTENSIONS = set(['csv', 'xlsx','pkl'])
    UPLOAD_FOLDER = 'D:/uploads'
    application.secret_key = "secret key"
    application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    application.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    application.run(host='0.0.0.0', debug=True)
