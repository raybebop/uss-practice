#!/usr/bin/env python
#-*-coding:utf8-*-

import os, sys, re
import requests

from bs4 import BeautifulSoup
from collections import OrderedDict

from ussBase import HTTP_HEADERS, http_get
from hkConfig import *

market_highlights = [
    ('Traded', re.compile('Traded: (\d+)')),
    ('Advanced', re.compile(r'Advanced\s+: (\d+)')), 
    ('Declined', re.compile(r'Declined\s+: (\d+)')),
    ('Unchanged', re.compile(r'Unchanged\s+: (\d+)')),
    ('HK$', re.compile(r'\(HK\$\):\s+(.*)')),
    ('Shares', re.compile(r'\(Shares\):\s+(.*)')),
    ('Deals', re.compile(r'\(Deals\):\s+(.*)')),
    ('CNY', re.compile(r'\(CNY\):\s+(.*)')),
]

def dataExtractor(raw):
    if raw:
        d = re.sub(r',', '', raw[0])
        try:
            return int(d)
        except:
            return -1
    else:
        return -255

def summaryAnalyzer(ds):
    records = map(lambda x: x.encode('utf8'), ds.split('\r\n'))
    for r in records:
        for k,v in OrderedDict(market_highlights).items():
            if k in r:
                print k, '>>>', dataExtractor(re.findall(v, r))

def indexAnalyzer(di):
    return di

def dollarsAnalyzer(td):
    return td

def sharesAnalyzer(ti):
    return ti

def main():
    #url = HKEX_DAYQUOT_TPL % "180126"
    #print ">>>", url
    #res = http_get(url, HTTP_HEADERS)

    #if res.status_code == 200:
    #    html = res.content
    #    #print html
    #    #print json.dumps(html, indent=4)
    #else:
    #    print 'ERROR: get stock data failed'
    #    sys.exit(1)

    html = open('d180126e.htm', 'r').read()
    soup = BeautifulSoup(html, 'html.parser')
    mh = soup.find('a', attrs={'name':'market_highlights'})
    content = mh.next_sibling
    record = content.split(HKEX_DAYQUOT_SEP)

    daily_summary = record[0]
    daily_index = record[1]
    top10_by_dollars = record[2]
    top10_by_shares = record[3]

    summaryAnalyzer(daily_summary)
    print '='*77
    #print indexAnalyzer(daily_index)
    #print '='*77
    #print dollarsAnalyzer(top10_by_dollars)
    #print '='*77
    #print sharesAnalyzer(top10_by_shares)
    #print '='*77


if __name__ == '__main__':
    main()
