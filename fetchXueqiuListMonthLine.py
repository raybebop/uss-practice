#!/usr/bin/env python
#-*-coding:utf8-*-
#This Program fetch each stock's month lines since 2016-1-1 and insert data into usStock.db
#table ussMonthLine where marketcapital > 500,000,000

import os, sys, re
import json
import time
import random
import math
import requests
import sqlite3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from ussConf import *
from xueqiuLib import *
from fetchXueqiuKLine import *

def se_covert(n):
    "covert scientific enumeration to float"
    if type(n) == type(u'haha'):
        n = n.encode('utf-8')
    if type(n) == type('haha'):
        n = float(n)
    #return '%.f' % n
    return '{:.0f}'.format(n)

def generateSQL(symbol, name, monthLineData):
    sqlTemplate = 'INSERT INTO ussMonthLine (%s) VALUES (%s)'
    SQLList = []
    for i in monthLineData:
        i['symbol'] = symbol
        i['name'] = name 
        vs = map(lambda x: '"%s"' % x, i.values())
        SQLList.append(sqlTemplate % (','.join(i.keys()),  ','.join(vs)))
    #print SQLList
    return SQLList;

def insert_into(db, symbol, name, monthLineData):
    SQLList = generateSQL(symbol, name, monthLineData)
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("BEGIN")
    #map(cursor.execute(),SQLList)
    for i in SQLList:
        #print i
        cursor.execute(i)
    cursor.close()
    conn.commit()
    conn.close()

def level1Filter(filterSql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    temp = cursor.execute(filterSql)
    stockList = temp.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return stockList

def main():
    #set parameters of query
    now_ts = int(time.time())
    underline = now_ts*1000

    begin_dt = time.strptime('2016-01-01', '%Y-%m-%d')
    end_dt = time.localtime()
    begin_ts = int(time.mktime(begin_dt))*1000
    end_ts = int(time.mktime(end_dt))*1000
    underline = int(time.time())*1000

    #set cookie 
    _status, cookie = setCookie()
    if _status != 200:
        print 'ERROR: set cookie failed'
        sys.exit(1)
    HTTP_HEADERS['cookie'] = cookie

    #general the stock list where marketcaptial > 500,000,000
    filterSql = 'SELECT DISTINCT symbol,name from usslist where marketcapital>500000000'
    stockList = level1Filter(filterSql,'usStock.db')
    #print len(stockList),type(stockList)
    #print stockList
    #print stockList[0]

    #fetch stock data and insert monthline into usStock.db table ussMonthLine
    periodURI = STOCKDATA_MONTH_URI
    for i in stockList:
        symbol = i[0]
        name = i[1]
        print '----fetching monthdata of',symbol,name
        data = fetchKLine(symbol, begin_ts, end_ts, underline, HTTP_HEADERS, periodURI)
        #print type(data) it's a dict return from Xueqiu.
        #print data
        monthLineData = data['chartlist']
        #print type(monthLineData),monthLineData 
        #it is a list. 
        #print type(monthLineData[0]),monthLineData[0] 
        #it is a dict.
        print '----inserting monthdata of',symbol,name
        insert_into('usStock.db', symbol, name, monthLineData)
        time.sleep(1)
if __name__ == '__main__':
    main()
