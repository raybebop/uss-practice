#!/usr/bin/env python
#-*-coding:utf8-*-
#modified by rr

from ussBase import *
from datetime import datetime

def filterStocks():
    sql = 'SELECT distinct symbol from usslist '
    sql+= 'where marketcapital>5000000000 '
    rtv = dbExec('USSTOCK.db', sql)
    return rtv

def getLastNdays(symbol, n):
    sql = "select symbol,timestamp,volume,percent,amount/marketcapital "
    sql+= "from usslist where symbol='%s' " % symbol
    sql+= "order by timestamp desc limit %d" % n
    rtv = dbExec('USSTOCK.db', sql)
    return rtv

def genYmd(ts):
    return datetime.fromtimestamp(ts).strftime("%Y%m%d")

def calVol(vs):
    ts = 1
    vl = 2
    rtv = list()
    for i in range(len(vs)-1):
        dt = '%s-%s' % (genYmd(vs[i+1][ts]), genYmd(vs[i][ts]))
        try:
            tr = divmod(vs[i][vl]-vs[i+1][vl], vs[i+1][vl])
            pc = float('.'.join([str(x) for x in tr]))
        except:
            pc = 0
        #rtv.append((dt, pc))
        rtv.append(pc)
    return rtv

def main():
    stocklist = filterStocks()
    #dst = map(lambda x: (x[0], getLastNdays(x[0], 3)), stocklist[:-1])
    #for i in dst:
    #    r = calVol(i[1])
    #    print '%s,%s' % (i[0], ','.join([str(n) for n in r]))
    for i in stocklist[:-1]:
        symbol = i[0].encode('utf-8')
        dst = getLastNdays(symbol, 4)
        r = calVol(dst)
        print '%s,%s' % (symbol, ','.join([str(n) for n in r]))

if __name__ == '__main__':
    main()

