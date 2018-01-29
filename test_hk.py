#!/usr/bin/env python
#-*-coding:utf8-*-

import os, sys, re
import requests
from bs4 import BeautifulSoup

from ussBase import HTTP_HEADERS, http_get
from hkConfig import *

def main():
    url = HKEX_DAYQUOT_TPL % "180126"
    print ">>>", url
    res = http_get(url, HTTP_HEADERS)
    if res.status_code == 200:
        html = res.content
        print html
        #print json.dumps(html, indent=4)
    else:
        print 'ERROR: get stock data failed'
        sys.exit(1)

if __name__ == '__main__':
    main()
