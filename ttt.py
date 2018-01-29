#!/usr/bin/env python
#-*-coding:utf8-*-

import os, sys, re
import requests

from bs4 import BeautifulSoup
from collections import OrderedDict

from ussBase import HTTP_HEADERS, http_get
from hkConfig import *

market_highlights = OrderedDict()

def summaryAnalyzer(ds):
    records = map(lambda x: x.encode('utf8'), ds.split('\r\n'))
    for j in records:
        if 'Traded' in j:
            print 'Traded', re.findall(r'Traded: (\d+)', j)
        if 'Advanced' in j:
            print 'Advanced', re.findall(r'Advanced\s+: (\d+)', j)
        if 'Declined' in j:
            print 'Declined', re.findall(r'Declined\s+: (\d+)', j)
        if 'Unchanged' in j:
            print 'Unchanged', re.findall(r'Unchanged\s+: (\d+)', j)
        if 'HK$' in j:
            print 'HK$', re.findall(r'\(HK\$\):\s+(.*)', j)
        if 'Shares' in j:
            print 'Shares', re.findall(r'\(Shares\):\s+(.*)', j)
        if 'Deals' in j:
            print 'Deals', re.findall(r'\(Deals\):\s+(.*)', j)
        if 'CNY' in j:
            print 'CNY', re.findall(r'\(CNY\):\s+(.*)', j)


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
