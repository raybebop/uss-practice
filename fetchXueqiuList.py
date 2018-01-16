#!/usr/bin/env python
#-*-coding:utf8-*-

from ussBase import *

def generateSQL(stocks):
    sqlTemplate = 'INSERT INTO usslist (%s) VALUES (%s)'
    SQLList = []
    for i in stocks:
        i['timestamp'] = now_ts
        vs = map(lambda x: '"%s"' % x, i.values())
        SQLList.append(sqlTemplate % (','.join(i.keys()),  ','.join(vs)))
    #print SQLList
    return SQLList;

def insert_into(db, stocks):
    SQLList = generateSQL(stocks)
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

def main():
    _status, cookie = setCookie()
    if _status != 200:
        print 'ERROR: set cookie failed, http status is', _status
        sys.exit(1)
    HTTP_HEADERS['cookie'] = cookie

    work_path = os.path.dirname(os.path.realpath(__file__))
    global now_ts
    now_ts = int(time.time())
    underline = genTs(now_ts)
    size = 100

    for i in range(1, 105):
        query = {
            'UNDERLINE': underline,
            'SIZE': size,
            'PAGE': i,
        }
        url = genUrlByTemplate(HTTP_URI['stocklist'], query)
        res = http_get(url, HTTP_HEADERS)
        if res.status_code == 200:
            data  = json.loads(res.content)
            #print json.dumps(data, indent=4)
            stocks = data['stocks']
            if stocks:
                print 'page %d: insert into %s/USSTOCK.db' % (i, work_path)
                insert_into('%s/USSTOCK.db' % work_path, stocks) 
                time.sleep(1)
        else:
            print 'ERROR: get stock list failed, url=%s' % url
            sys.exit(1)


if __name__ == '__main__':
    main()
