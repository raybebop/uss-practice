#!/usr/bin/python
#-*-coding:utf8-*-                                                          
#This Program fetch each stock's month lines since 2016-1-1 and insert data
#into usStock.db
#table ussMonthLine where marketcapital > 500,000,000                       
import sqlite3
import operator
import time
import datetime
import matplotlib
#set matplotlib.use('Agg') to avoid DISPLAY problem
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from matplotlib.pyplot import savefig,figure
from pandas import Series
import sys
from stockFilter import stockFilter

def selectData(DB, periodTable):
    selectSQL = 'SELECT timestamp,ma30 from %s order by timestamp' % periodTable
    #print selectSQL
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    temp = cursor.execute(selectSQL)
    tempData = temp.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    for i in range(len(tempData)):
        tempData[i] = [tempData[i][0]/1000, tempData[i][1]]
    return tempData

#convert timestamp to datetime obj so that plot can work with it.
def convertTimeToDate(l):
    lWithDate = []
    #tempTime = time.localtime(i[0]/1000)
    #i[0] = time.strftime('%Y-%m-%d', tempTime)
    for i in range(len(l)):
        tempTime = l[i][0]
        tempDate = datetime.date.fromtimestamp(tempTime)
        lWithDate.append([tempDate, l[i][1]])
    return lWithDate

def brief(l):
    #l is a list which is consist of inflection points
    tempList = []
    init = l.pop(0)
    tempList.append(init)
    while len(l) > 0:
        nextElement = l.pop(0)
        priceGap = init[1] - nextElement[1]
        dateGap = init[0] - nextElement[0]
        if abs(dateGap.days) < 10 and priceGap < 0.05:
            pass
        else:
            tempList.append(nextElement)
        init = nextElement

    return tempList

def inflection(l):
    #l is a list which is consist of basic data of a stock
    #return inflection points as a list
    first = l[0]
    last = l[-1]
    init = l.pop(0)
    inflectionPoints = []
    initTrend = 2

    while len(l) > 0:
        nextItem = l.pop(0)
        if init[1] > nextItem[1]:
           trend = -1
        elif init[1] < nextItem[1]:
            trend = 1
        else:
            trend = 0

        if trend == initTrend: 
            pass
        else:
            inflectionPoints.append(init)

        initTrend = trend
        init = nextItem

    inflectionPoints.append(last)
    return inflectionPoints 

def briefInflection(l):
    #deal inflectionPoints by slope and xDistance.
    init = l.pop(0)
    last = l[-1]
    briefInflectionPoints = []
    briefInflectionPoints.append(init)
    #print 'the first element of briefInflectionPoints is:',briefInflectionPoints

    while len(l) > 0:
        nextItem = l.pop(0)
        xDistance = (nextItem[0] - init[0]).days
        yDistance = nextItem[1] - init[1]
        if yDistance > 0:
            slope = (yDistance/init[1])/xDistance
        elif yDistance < 0:
            slope = (yDistance/nextItem[1])/xDistance
        else:
            slope = 0

        if xDistance > 10:
            briefInflectionPoints.append(init)
            briefInflectionPoints.append(nextItem)
            #print init,nextItem,'-'*10,'the slope is:',slope,abs(slope)
        elif slope > 0.004 and xDistance > 2:
            briefInflectionPoints.append(init)
            briefInflectionPoints.append(nextItem)
            #print init,nextItem,'-'*10,'the slope is:',slope,abs(slope)
        elif slope < -0.002 and xDistance > 2:
            briefInflectionPoints.append(init)
            briefInflectionPoints.append(nextItem)
            #print init,nextItem,'-'*10,'the slope is:',slope,abs(slope)
        else:
            #print init,nextItem,'^'*5,slope
            pass

        init = nextItem
    briefInflectionPoints.append(last)
    return briefInflectionPoints

def stockAnalysis(symbol):
    #symbol = 'AAOI'
    DB = '/home/whj/bin/uss/stockDBs/%s.db' % symbol
    #DB = '/home/whj/bin/uss/stockDBs/AMBA.db'
    print symbol,DB,'--'*5
    periodTable = 'ussDayLine'
    ma20List = selectData(DB, periodTable)
    #print type(ma20List)
    #print ma20List
    #max(maDict.items(), key=operator.itemgetter(1))
    #max(maData, key=operator.itemgetter(1))

    ma20WithDate = convertTimeToDate(ma20List)
    #print ma20WithDate
    first = ma20WithDate[0]
    last = ma20WithDate[-1]

    plt.figure(figsize=(16,10))
    plt.title(symbol)
    x = [i[0] for i in ma20WithDate]
    y = [i[1] for i in ma20WithDate]
    plt.plot(x, y, color="orange", linewidth=1.0, linestyle="-", marker="^")


    inflectionPoints = inflection(ma20WithDate)

    x = [i[0] for i in inflectionPoints]
    y = [i[1] for i in inflectionPoints]
    plt.plot(x, y, color="blue", linewidth=1.0, linestyle="-", marker="o")

    briefInflectionPoints = briefInflection(inflectionPoints)
    print 'the original length of briefinflectionPoints is:',len(briefInflectionPoints)
    briefInflectionPoints = brief(briefInflectionPoints)
    briefInflectionPoints = inflection(briefInflectionPoints)
    print 'the length of briefinflectionPoints is:',len(briefInflectionPoints)

    x = [i[0] for i in briefInflectionPoints]
    y = [i[1] for i in briefInflectionPoints]
    #print x
    #print y
    plt.plot(x, y, color="red", linewidth=2.0, linestyle="--", marker="^")
    picture = './img/brief%s.png' % symbol
    savefig(picture)
    plt.close()

def main():
    print "Going to get stockList by filter------"
    stockList = stockFilter('usStock.db')
    for i in stockList:
        symbol,name = i[0],i[1]
        print symbol,name
        print "Going to process %s,%s" % (symbol,name)
        stockAnalysis(symbol)


if __name__ == '__main__':
    main()
