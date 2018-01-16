#!/usr/bin/env python
#-*-coding:utf8-*-                                                          
#This Program fetch each stock's month lines since 2016-1-1 and insert data
#into usStock.db
#table ussMonthLine where marketcapital > 500,000,000                       

import sqlite3
import json

def stockFilter(db):
    filterSQL = 'SELECT DISTINCT symbol,name from usslist where '
    filterSQL += 'marketcapital>500000000 and '
    filterSQL += 'amount/marketcapital>0.01 and '
    filterSQL += '(high52w-low52w)/current>0.5'
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    temp = cursor.execute(filterSQL)
    stockList = temp.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return stockList

def main():
    stockList = stockFilter('USSTOCK.db')
    print json.dumps(stockList, indent=4)

if __name__ == '__main__':
    main()

