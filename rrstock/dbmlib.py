#-*-coding:utf8-*-
'''
database/table/sql management library
'''

import os, sys
import sqlite3

#def truncateTable(DB):
#    conn = sqlite3.connect(DB)
#    cursor = conn.cursor()
#    cursor.execute("BEGIN")
#    tables = ['ussDayLine', 'ussWeekLine', 'ussMonthLine']
#    for i in tables:
#        SQL = 'DELETE FROM %s;' % i
#        #print SQL
#        cursor.execute(SQL)
#    cursor.execute('VACUUM;')
#    cursor.close()
#    conn.commit()


class SqliteHandler(object):
    def __init__(self, dbfile):
        if os.path.isfile(dbfile):
            self.dbexist = True
        else:
            self.dbexist = False
        self.dbfile = dbfile
        self.list_tables = "SELECT name FROM sqlite_master WHERE type='table'"
        self.drop_table = "DROP TABLE IF EXISTS %s"
    def conn(self):
        return sqlite3.connect(self.dbfile)
    #def cursor(self):
    #    self.cursor = self.conn.cursor()
    #def list_tables(self):
    #    _sql = 'show tables'
    #    return self.cursor.execute(_sql)
    #def execute(self, sql):
    #    return self.cursor(sql)
    #def fetchall(self, ex):
    #    return ex.fetchall()
    #def close():
    #    self.cursor.close()
    #    self.conn.commit()
    #    self.conn.close()

STOCK_LIST_TPL = '''
create table if not exists %s (
    symbol  VARCHAR(28),
    code    VARCHAR(28),
    name    VARCHAR(28),
    'current' REAL,
    percent REAL,
    change  REAL,
    high    REAL,
    low REAL,
    high52w REAL,
    low52w  REAL,
    marketcapital   BIGINT,
    amount  REAL,
    'type'    INT,
    pettm   REAL,
    volume  BIGINT,
    hasexist    BOOL,
    ctime TIMESTAMP NOT NULL DEFAULT (datetime('now','localtime'))
);
'''

STOCK_DATA_TPL = '''
create table if not exists %s (
    symbol  VARCHAR(28),
    name    VARCHAR(28),
    volume BIGINT,
    open REAL,
    high REAL,
    close REAL,
    low REAL,
    chg REAL,
    percent REAL,
    turnrate REAL,
    ma5 REAL,	
    ma10 REAL,	
    ma20 REAL,	
    ma30 REAL,	
    dif REAL,
    dea REAL,
    macd REAL,
    lot_volume BIGINT,
    timestamp INTEGER,
    time TEXT	
);
'''
