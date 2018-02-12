#-*-coding:utf8-*-
'''
utilities library
'''

import time
import string

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class UriTemplate(string.Template):  
    delimiter = '%'  

def genUrlByTemplate(tpl, val):
    return UriTemplate(tpl).safe_substitute(val)

def genTs(n):
    return n*1000 if isinstance(n, (int, float)) else 0

def compare_two_lists(a, b):
    intersection = set(a).intersection(b)
    union = set(a).union(b)
    return intersection, union

def chomp(s):
    return s.rstrip('\n|\r\n')

def http_get(url, headers):
    return requests.get(
        url,
        headers = headers,
        allow_redirects = False,
        verify = True,
    )

def set_cookie(url, headers):
    try:
        r = http_get(url, headers)
        return r.status_code, r.headers['set-cookie']
    except Exception, e:
        return 600, str(e)

def time_now_fmt():
    "time now by defined format"
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def time_now_its():
    "time now by integer timestamp"
    return int(time.time())

def se_convert(n):
    "covert scientific enumeration to float"
    if type(n) == type(u'haha'):
        n = n.encode('utf-8')
    if type(n) == type('haha'):
        n = float(n)
    #return '%.f' % n
    return '{:.0f}'.format(n)
