#!/usr/bin/env python
#-*-coding:utf8-*-

import os, sys, re
import requests

from bs4 import BeautifulSoup
from collections import OrderedDict

from ussBase import HTTP_HEADERS, http_get, time_now
from hkConfig import *

def summaryAnalyzer(ds):
    result = OrderedDict()
    summary_regexp = [
        ('Traded', re.compile('Traded: (\d+)')),
        ('Advanced', re.compile('Advanced\s+: (\d+)')), 
        ('Declined', re.compile('Declined\s+: (\d+)')),
        ('Unchanged', re.compile('Unchanged\s+: (\d+)')),
        ('HK$', re.compile('\(HK\$\):\s+(.*)')),
        ('Shares', re.compile('\(Shares\):\s+(.*)')),
        ('Deals', re.compile('\(Deals\):\s+(.*)')),
        ('CNY', re.compile('\(CNY\):\s+(.*)')),
    ]
    records = map(lambda x: x.encode('utf8'), ds.split('\r\n'))
    for r in records:
        for k,v in OrderedDict(summary_regexp).items():
            if k in r:
                vv = re.findall(v, r)
                if vv:
                    try:
                        d = re.sub(r',', '', vv[0])
                        result[k] = int(d)
                    except:
                        result[k] = -1
                else:
                    result[k] = -255
    return result

def indexAnalyzer(di):
    result = OrderedDict()
    index_regexp = [
        ('HANG SENG INDEX', re.compile('\s+HANG SENG INDEX\s+(.*)')),
        ('ENTERPRISES INDEX', re.compile('\s+ENTERPRISES INDEX\s+(.*)')),
    ]
    records = map(lambda x: x.encode('utf8'), di.split('\r\n'))
    for r in records:
        for k,v in OrderedDict(index_regexp).items():
            if k in r:
                vv = re.findall(v, r)
                kk = re.sub(r' ', '', k[:-6])
                if vv:
                    result[kk] = map(
                        lambda x: float(x),
                        re.sub(r'\s+', ' ', vv[0]).split(' ')
                    )
                else:
                    result[kk] = []
    return result

def dollarsAnalyzer(td):
    result = OrderedDict()
    records = map(lambda x: x.encode('utf8'), td.split('\r\n'))
    for r in records:
        if ' HKD ' in r:
            rr = r.split('HKD')
            ss = re.sub(r'^\s+|\s+$', '', rr[0]).split(' ', 1)
            code = ss[0]
            name = ss[1]
            quota = re.sub(r'\s+', ' ', rr[1]).split(' ')
            quota = filter(None, quota)
            quota = map(lambda x: float(re.sub(r',', '', x)), quota)
            quota.insert(0, name)
            result[code] = quota
    return result

def sharesAnalyzer(ts):
    return ts

def main():
    #html = open(sys.argv[1], 'r').read()

    #tn = time_now()
    #ts = re.sub(r'[-|:]', '', tn)
    #print ts[2:8]
    #sys.exit()

    url = HKEX_DAYQUOT_TPL % "180129"
    print ">>>", url
    res = http_get(url, HTTP_HEADERS)
    if res.status_code == 200:
        html = res.content
        #print html
        #print json.dumps(html, indent=4)
    else:
        print 'ERROR: get stock data failed'
        sys.exit(1)

    soup = BeautifulSoup(html, 'html.parser')
    mh = soup.find('a', attrs={'name':'market_highlights'})
    content = mh.next_sibling
    record = content.split(HKEX_DAYQUOT_SEP)

    daily_summary = record[0]
    daily_index = record[1]
    top10_by_dollars = record[2]
    top10_by_shares = record[3]

    for k,v in summaryAnalyzer(daily_summary).items():
        print k, '>>>', v
    print '='*77
    for k,v in indexAnalyzer(daily_index).items():
        print k, '>>>', v
    print '='*77
    for k,v in dollarsAnalyzer(top10_by_dollars).items():
        print k, '>>>', v
    print '='*77

if __name__ == '__main__':
    main()
