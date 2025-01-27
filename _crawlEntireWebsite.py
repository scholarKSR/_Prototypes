#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 21:23:00 2019

@author: k as root
"""
import requests
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    
    url='http://en.wikipedia.org'+pageUrl # ----------< INPUT >
    
    r = requests.get(url) # use try catch  # MY RESEARCH : "OBJECT" r
    bsObj = BeautifulSoup(r.text,'html.parser')
    
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")
    
    for link in bsObj.findAll("a",href=re.compile("/wiki/")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # We have encountered a new page
                newPage = link.attrs['href']
                print("-----------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")


# we can use sys.argv to create a composite command for the program
# eg. python _crawlEntireWebsite www.wikipidea.org