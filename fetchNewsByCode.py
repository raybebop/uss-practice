#!/usr/bin/python
#-*-coding:utf8-*-                                                          
#This Program fetch finance data from internet. 
#such as https://finviz.com/quote.ashx?t=AKS
#into db

import sqlite3
import operator
import time
import datetime
from stockFilter import stockFilter
import os, sys, re
import string
import requests
import json
from ussConf import *
from bs4 import BeautifulSoup

def mainTableParse(table):
    keys= []
    values = []
    for row in table:
        keySet = row.findAll('td', class_='snapshot-td2-cp')
        for i in keySet:
             keys.append(i.get_text())
        valueSet = row.findAll('td', class_='snapshot-td2')
        for i in valueSet:
            values.append(i.get_text())
    dataSet = dict(zip(keys, values))
    for k,v in dataSet.items():
        print "[%s]=" % k,v

def ratingTableParse(table):
    ratingSet = []
    for row in table:
        rating = []
        data = row.find_all('td')
        for i in data:
            rating.append(i.get_text())
        ratingSet.append(rating)
    #print ratingSet
    for i in ratingSet:
         print i

def newsTableParse(table):
    newsSet = []
    for row in table:
        print row.get_text()
        print '='*69

def main():
    if len(sys.argv) < 2:
        print 'ERROR: please input ticker like BABA,AMD,FB,NVDA...'
        sys.exit(1)

    symbol = sys.argv[1].upper()
    URL = 'https://finviz.com/quote.ashx?t=%s' % symbol
    print URL

    res = requests.get(URL)
    if res.status_code == 200:
        html = res.content
        #print json.dumps(data, indent=4)
    else:
        print 'ERROR: get stock data failed'
        sys.exit(1)
    soup = BeautifulSoup(html, "html.parser")

    ##parse the main table which is consist of lots of basic data
    #basicTable = soup.find_all('tr', class_='table-dark-row')
    #mainTableParse(basicTable)
    #print '--'*50
    ##parse the rating table
    #ratingTable = soup.find_all('td', class_='fullview-ratings-inner')
    ##ratingTable contains multipul rows which to be passed to ratingTableParse
    #ratingTableParse(ratingTable)

    newsTable = soup.find_all('table', class_='fullview-news-outer')
    newsTableParse(newsTable)

if __name__ == '__main__':
    main()
