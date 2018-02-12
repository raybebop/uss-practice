#-*-coding:utf8-*-
'''
xueqiu library
'''

import time

XQ_HOMEPAGE_URI = 'https://xueqiu.com'

XQ_USSTOCKLIST_URI = 'https://xueqiu.com/stock/cata/stocklist.json?page=%PAGE&size=%SIZE&order=desc&orderby=percent&type=0%2C1%2C2%2C3&isdelay=1&_=%UNDERLINE'

XQ_HKSTOCKLIST_URI = 'https://xueqiu.com/stock/cata/stocklist.json?page=%PAGE&size=%SIZE&order=desc&orderby=percent&type=30&isdelay=1&_=%UNDERLINE'

XQ_STOCKDATA_URI = 'https://xueqiu.com/stock/forchartk/stocklist.json?symbol=%SYMBOL&period=%PERIOD&type=normal&begin=%BEGIN_TS&end=%END_TS&_=%UNDERLINE'

def gen_xq_ts(begin_date, end_date):
    '''generate timestamp by begin and end date like: gen_xq_ts('2014-01-01','2018-01-01')'''
    if begin_date:
        begin_dt = time.strptime(begin_date, '%Y-%m-%d')
    else:
        begin_dt = time.strptime('2012-01-01', '%Y-%m-%d')
    if end_date:
        end_dt = time.strptime(end_date, '%Y-%m-%d')
    else:
        end_dt = time.localtime()
    begin_ts = int(time.mktime(begin_dt))*1000
    end_ts = int(time.mktime(end_dt))*1000
    underline = int(time.time())*1000
    return begin_ts, end_ts, underline

