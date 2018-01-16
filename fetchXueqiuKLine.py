#!/usr/bin/env python
#-*-coding:utf8-*-
#functions of getting day/week/month k-line of stock
#modified by rr

from ussBase import *

def fetchKLine(symbol, period, begin_date):
    _status, cookie = setCookie()
    if _status != 200:
        print 'ERROR: set cookie failed'
        sys.exit(1)
    HTTP_HEADERS['cookie'] = cookie

    begin_dt = time.strptime(begin_date, '%Y-%m-%d')
    end_dt = time.localtime()
    begin_ts = int(time.mktime(begin_dt))*1000
    end_ts = int(time.mktime(end_dt))*1000
    underline = int(time.time())*1000

    query = {
        'SYMBOL': symbol,
        'PERIOD': period,
        'BEGIN_TS': begin_ts,
        'END_TS': end_ts,
        'UNDERLINE': underline,
    }
    url = genUrlByTemplate(HTTP_URI['stockdata'], query)
    #print url
    res = http_get(url, HTTP_HEADERS)
    return res

def main():
    valid_period = ['day', 'week', 'month']
    try:
        period = sys.argv[1]
    except Exception,e:
        print 'Usage: %s [%s]\n' % (sys.argv[0], '|'.join(valid_period))
        raise e
    if period not in valid_period:
        print 'Usage: %s [day|week|month]\n' % sys.argv[0]
        sys.exit(1)

    res = fetchKLine('WB', period, '2017-01-01')
    if res.status_code == 200:
        data = json.loads(res.content)
        print json.dumps(data, indent=4)
    else:
        print 'ERROR: get stock data failed'
        print res.text
        sys.exit(1)

if __name__ == '__main__':
    main()
