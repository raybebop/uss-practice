#!/usr/bin/env python
#-*-coding:utf8-*-                                                          

import sqlite3
import os
import sys
import time
from ussConf import *
from xueqiuLib import *
from stockFilter import stockFilter
from fetchXueqiuKLine import fetchKLine 

def fetchComboData(symbol, HTTP_HEADERS):

    begin_dt = time.strptime('2016-01-01', '%Y-%m-%d')
    end_dt = time.localtime()
    begin_ts = int(time.mktime(begin_dt))*1000
    end_ts = int(time.mktime(end_dt))*1000
    underline = int(time.time())*1000

    periodURI = STOCKDATA_DAY_URI
    dayData = fetchKLine(symbol, begin_ts, end_ts, underline, HTTP_HEADERS, periodURI)
    dayData['periodTable'] = 'ussDayLine'
    #print 'dayData is:', type(dayData)
    #print 'periodTable is:',dayData['periodTable']

    periodURI = STOCKDATA_WEEK_URI
    weekData = fetchKLine(symbol, begin_ts, end_ts, underline, HTTP_HEADERS, periodURI)
    weekData['periodTable'] = 'ussWeekLine'
    periodURI = STOCKDATA_MONTH_URI
    monthData = fetchKLine(symbol, begin_ts, end_ts, underline, HTTP_HEADERS, periodURI)
    monthData['periodTable'] = 'ussMonthLine'

    comboData = [dayData, weekData, monthData]
    return comboData

def generateSQL(symbol, name, comboData):
    sqlTemplate = 'INSERT INTO %s (%s) VALUES (%s)'
    SQLList = []
    #comboData is a list consisted of day,week,month data which are actually dicts
    for i in comboData:
        periodTable = i['periodTable']
        for j in i['chartlist']:
            j['symbol'] = symbol
            j['name'] = name 
            vs = map(lambda x: '"%s"' % x, j.values())
            SQLList.append(sqlTemplate % (periodTable, ','.join(j.keys()), ','.join(vs)))
    #print SQLList
    return SQLList;



def insertComboData(DB, symbol, name, comboData):
    SQLList = generateSQL(symbol, name, comboData)
    print 'SQLList is',type(SQLList),len(SQLList)
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("BEGIN")
    #map(cursor.execute(),SQLList)
    for i in SQLList:
        #print i
        cursor.execute(i)
    cursor.close()
    conn.commit()

def truncateTable(DB):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("BEGIN")
    tables = ['ussDayLine', 'ussWeekLine', 'ussMonthLine']
    for i in tables:
        SQL = 'DELETE FROM %s;' % i
        #print SQL
        cursor.execute(SQL)
    cursor.execute('VACUUM;')
    cursor.close()
    conn.commit()

def main():
    _status, cookie = setCookie()
    if _status != 200:
        print 'ERROR: set cookie failed'
        sys.exit(1)
    HTTP_HEADERS['cookie'] = cookie

    stockList = stockFilter('usStock.db')
    #print type(stockList)
    #print stockList

    print '--------------------------------------------------------------'
    for i in stockList:
        symbol, name = i[0], i[1]
        DB = './stockDBs/' + symbol + '.db'
        if os.path.isfile(DB):
            print ('there is %s, going to truncate Tables and download data of %s'
                   % (DB,symbol))
            truncateTable(DB)
            comboData = fetchComboData(symbol, HTTP_HEADERS)
            #generateSQL(symbol, name, comboData)
            insertComboData(DB, symbol, name, comboData)
            print '--------------------------------------------------------------'
        else:
            print ('there is no %s DB, Creating %s and tables'
                   % (DB, DB))
            createDBCommand = 'sqlite3 %s < ./ussData.sql' % DB
            #sys.exit(1)
            #print createDBCommand
            os.system(createDBCommand)
            comboData = fetchComboData(symbol, HTTP_HEADERS)
            #generateSQL(symbol, name, comboData)
            insertComboData(DB, symbol, name, comboData)
            print '--------------------------------------------------------------'

    print 'The Data of All Stocks of the List has been downloaded' 

if __name__ == '__main__':
    main()
