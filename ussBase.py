#-*-coding:utf8-*-

import os, sys, re
import sqlite3
import string
import json
import time
import math

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class xueqiuLib(object):
    def __init__(self):
        self.HTTP_HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
            'Content-type': 'application/x-www-form-urlencoded',
            'cookie': setCookie()[-1]
        }
        self.HTTP_URI = {
            'homepage': 'https://xueqiu.com',
            'stocklist': 'https://xueqiu.com/stock/cata/stocklist.json?page=%PAGE&size=%SIZE&order=desc&orderby=percent&type=0%2C1%2C2%2C3&isdelay=1&_=%UNDERLINE',
            'stockdata': 'https://xueqiu.com/stock/forchartk/stocklist.json?symbol=%SYMBOL&period=%PERIOD&type=normal&begin=%BEGIN_TS&end=%END_TS&_=%UNDERLINE',
        }


HTTP_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
    'Content-type': 'application/x-www-form-urlencoded',
}

HOMEPAGE_URI = 'https://xueqiu.com'

STOCKLIST_URI = 'https://xueqiu.com/stock/cata/stocklist.json?page=%PAGE&size=%SIZE&order=desc&orderby=percent&type=0%2C1%2C2%2C3&isdelay=1&_=%UNDERLINE'

STOCKDATA_URI = 'https://xueqiu.com/stock/forchartk/stocklist.json?symbol=%SYMBOL&period=%PERIOD&type=normal&begin=%BEGIN_TS&end=%END_TS&_=%UNDERLINE'

HTTP_URI = {
    'homepage': 'https://xueqiu.com',
    'stocklist': 'https://xueqiu.com/stock/cata/stocklist.json?page=%PAGE&size=%SIZE&order=desc&orderby=percent&type=0%2C1%2C2%2C3&isdelay=1&_=%UNDERLINE',
    'stockdata': 'https://xueqiu.com/stock/forchartk/stocklist.json?symbol=%SYMBOL&period=%PERIOD&type=normal&begin=%BEGIN_TS&end=%END_TS&_=%UNDERLINE',
}

class sqliteHandler(object):
    def __init__(self, dbfile):
        self.dbfile = dbfile
    def conn(self):
        self.conn = sqlite3.connect(dbfile)
        self.cursor = conn.cursor
    def execute(self, sql):
        return self.cursor(sql)
    def fetchall(self, ex):
        return ex.fetchall()
    def close():
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

def dbExec(db, sql):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    e = cursor.execute(sql)
    values = e.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return values 

def se_covert(n):
    "covert scientific enumeration to float"
    if type(n) == type(u'haha'):
        n = n.encode('utf-8')
    if type(n) == type('haha'):
        n = float(n)
    #return '%.f' % n
    return '{:.0f}'.format(n)

class uriTemplate(string.Template):  
    delimiter = '%'  

def genUrlByTemplate(tpl, val):
    return uriTemplate(tpl).safe_substitute(val)

def genTs(n):
    return n*1000 if isinstance(n, (int, float)) else 0

def http_get(url, headers):
    return requests.get(
        url,
        headers = headers,
        allow_redirects = False,
        verify = True,
    )

def setCookie():
    try:
        r = http_get(HOMEPAGE_URI, HTTP_HEADERS)
        return r.status_code, r.headers['set-cookie']
    except Exception, e:
        return 600, str(e)

if __name__ == '__main__':
    haha = xueqiuLib()
    print haha.HTTP_HEADERS
    print haha.HTTP_URI
