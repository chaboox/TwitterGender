# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:51:49 2019

@author: deboosere_am
"""

import time
import operator
import unicodecsv as cs
import json
import msvcrt
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getTweets(timet):
    browser = webdriver.Chrome()
    base_url = u'https://twitter.com/search?l=fr&q='
    newlist = []
    y = []
    #maleName = [u'Alain', u'François', u'Julien', u'Stéphane', u'Olivier', u'Leo', u'Mathieu', u'Maxime', u'Thomas', u'Nico']
    #femalName = [u'Jeanne', u'Nathalie', u'Isabelle', u'Lucie', u'Manon', u'Lea', u'Alice', u'Emeline', u'Charlotte', u'Morgane']
    femalName = [ u'Lucie']
    maleName = [u'Alain']
    for male in femalName:
        query = male
        print(male)
        url = base_url + query
    
        browser.get(url)
        time.sleep(1)
    
        body = browser.find_element_by_tag_name('body')
    
        for ls in range(timet*5):
            print(ls)
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
        
        tweets = browser.find_elements_by_class_name("tweet-text")
        names = browser.find_elements_by_class_name("show-popup-with-id")
        aas = browser.find_elements_by_class_name("tweet")
    
       
        i = 0
        for a in aas:
            replyB = 'nop'
            #image = a.find_element_by_tag_name("img")
            tweeta = a.find_elements_by_class_name("tweet-text")
            #name = a.find_elements_by_class_name("fullname")
           # username = a.find_elements_by_class_name("username")
            reply = a.find_elements_by_class_name("ReplyingToContextBelowAuthor")
            #urllib.request.urlretrieve(image.get_attribute("src"), "male2/" +username[0].text +".jpg")
            if len(reply) > 0:
                replyB = 'WOUHOU'
            i = i +1
           # print(str(i) + ' ----- ' + image.get_attribute("src") + '   KKKKKK  ' + tweeta[0].text + '  OOOO   ' + replyB + 'USER ' + username[0].text +' NAME ' + name[0].text )
            if tweeta[0].text != None:
                if not(operator.contains(tweeta[0].text.lower(), male.lower())):
                    if replyB != 'WOUHOU':
                        if len(tweeta[0].text.split()) >10:
                            newlist.append(tweeta[0].text)
                            y.append(0)
                        
    for male in maleName:
        query = male
        print(male)
        url = base_url + query
    
        browser.get(url)
        time.sleep(1)
    
        body = browser.find_element_by_tag_name('body')
    
        for ls in range(timet*3):
            print(ls)
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
        
        tweets = browser.find_elements_by_class_name("tweet-text")
        names = browser.find_elements_by_class_name("show-popup-with-id")
        aas = browser.find_elements_by_class_name("tweet")
    
       
        i = 0
        for a in aas:
            replyB = 'nop'
            #image = a.find_element_by_tag_name("img")
            tweeta = a.find_elements_by_class_name("tweet-text")
            #name = a.find_elements_by_class_name("fullname")
           # username = a.find_elements_by_class_name("username")
            reply = a.find_elements_by_class_name("ReplyingToContextBelowAuthor")
            #urllib.request.urlretrieve(image.get_attribute("src"), "male2/" +username[0].text +".jpg")
            if len(reply) > 0:
                replyB = 'WOUHOU'
            i = i +1
           # print(str(i) + ' ----- ' + image.get_attribute("src") + '   KKKKKK  ' + tweeta[0].text + '  OOOO   ' + replyB + 'USER ' + username[0].text +' NAME ' + name[0].text )
            if tweeta[0].text != None:
                if not(operator.contains(tweeta[0].text.lower(), male.lower())):
                    if replyB != 'WOUHOU':
                        if len(tweeta[0].text.split()) >10:
                            newlist.append(tweeta[0].text)
                            y.append(1)
           
    return (newlist, y)

def getTweets2(timet, mannames, womennames, language, mintweet):
    browser = webdriver.Chrome()
    base_url = u'https://twitter.com/search?l=' + language + '&q='
    newlist = []
    y = []
    #maleName = [u'Alain', u'François', u'Julien', u'Stéphane', u'Olivier', u'Leo', u'Mathieu', u'Maxime', u'Thomas', u'Nico']
    #femalName = [u'Jeanne', u'Nathalie', u'Isabelle', u'Lucie', u'Manon', u'Lea', u'Alice', u'Emeline', u'Charlotte', u'Morgane']
    femalName = womennames.split()
    maleName = mannames.split()
    for male in femalName:
        query = male
        print(male)
        url = base_url + query
    
        browser.get(url)
        time.sleep(1)
    
        body = browser.find_element_by_tag_name('body')
    
        for ls in range(timet*1):
            print(ls)
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
        
        tweets = browser.find_elements_by_class_name("tweet-text")
        names = browser.find_elements_by_class_name("show-popup-with-id")
        aas = browser.find_elements_by_class_name("tweet")
    
       
        i = 0
        for a in aas:
            replyB = 'nop'
            #image = a.find_element_by_tag_name("img")
            tweeta = a.find_elements_by_class_name("tweet-text")
            #name = a.find_elements_by_class_name("fullname")
           # username = a.find_elements_by_class_name("username")
            reply = a.find_elements_by_class_name("ReplyingToContextBelowAuthor")
            #urllib.request.urlretrieve(image.get_attribute("src"), "male2/" +username[0].text +".jpg")
            if len(reply) > 0:
                replyB = 'WOUHOU'
            i = i +1
           # print(str(i) + ' ----- ' + image.get_attribute("src") + '   KKKKKK  ' + tweeta[0].text + '  OOOO   ' + replyB + 'USER ' + username[0].text +' NAME ' + name[0].text )
            if tweeta[0].text != None:
                if not(operator.contains(tweeta[0].text.lower(), male.lower())):
                    if replyB != 'WOUHOU':
                        if len(tweeta[0].text.split()) > mintweet:
                            newlist.append([tweeta[0].text, "Femme"])
                            y.append(0)
                        
    for male in maleName:
        query = male
        print(male)
        url = base_url + query
    
        browser.get(url)
        time.sleep(1)
    
        body = browser.find_element_by_tag_name('body')
    
        for ls in range(timet*1):
            print(ls)
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
        
        tweets = browser.find_elements_by_class_name("tweet-text")
        names = browser.find_elements_by_class_name("show-popup-with-id")
        aas = browser.find_elements_by_class_name("tweet")
    
       
        i = 0
        for a in aas:
            replyB = 'nop'
            #image = a.find_element_by_tag_name("img")
            tweeta = a.find_elements_by_class_name("tweet-text")
            #name = a.find_elements_by_class_name("fullname")
           # username = a.find_elements_by_class_name("username")
            reply = a.find_elements_by_class_name("ReplyingToContextBelowAuthor")
            #urllib.request.urlretrieve(image.get_attribute("src"), "male2/" +username[0].text +".jpg")
            if len(reply) > 0:
                replyB = 'WOUHOU'
            i = i +1
           # print(str(i) + ' ----- ' + image.get_attribute("src") + '   KKKKKK  ' + tweeta[0].text + '  OOOO   ' + replyB + 'USER ' + username[0].text +' NAME ' + name[0].text )
            if tweeta[0].text != None:
                if not(operator.contains(tweeta[0].text.lower(), male.lower())):
                    if replyB != 'WOUHOU':
                        if len(tweeta[0].text.split()) > mintweet:
                            newlist.append([tweeta[0].text, "Homme"])
                            y.append(1)
           
    return (newlist, y)



