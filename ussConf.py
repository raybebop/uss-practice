#-*-coding:utf8-*-

import os, sys, re
import string
import requests

HTTP_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
    'Content-type': 'application/x-www-form-urlencoded',
}

HOMEPAGE_URI = 'https://xueqiu.com'

STOCKLIST_URI = 'https://xueqiu.com/stock/cata/stocklist.json?page=%PAGE&size=%SIZE&order=desc&orderby=percent&type=0%2C1%2C2%2C3&isdelay=1&_=%UNDERLINE'

STOCKDATA_URI = 'https://xueqiu.com/stock/forchartk/stocklist.json?symbol=%SYMBOL&period=%PERIOD&type=normal&begin=%BEGIN_TS&end=%END_TS&_=%UNDERLINE'

STOCKDATA_DAY_URI = 'https://xueqiu.com/stock/forchartk/stocklist.json?symbol=%SYMBOL&period=1day&type=normal&begin=%BEGIN_TS&end=%END_TS&_=%UNDERLINE'
STOCKDATA_WEEK_URI ='https://xueqiu.com/stock/forchartk/stocklist.json?symbol=%SYMBOL&period=1week&type=normal&begin=%BEGIN_TS&end=%END_TS&_=%UNDERLINE'
STOCKDATA_MONTH_URI ='https://xueqiu.com/stock/forchartk/stocklist.json?symbol=%SYMBOL&period=1month&type=normal&begin=%BEGIN_TS&end=%END_TS&_=%UNDERLINE'

