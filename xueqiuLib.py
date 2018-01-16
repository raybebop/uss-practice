#-*-coding:utf8-*-

import os, sys, re
import string
import requests

from ussConf import *

class uriTemplate(string.Template):  
    delimiter = '%'  

def genUrlByTemplate(tpl, val):
    t = uriTemplate(tpl)
    return t.safe_substitute(val)

def setCookie():
    try:
        r = requests.get(
                HOMEPAGE_URI,
                headers = HTTP_HEADERS,
                allow_redirects = False,
                verify = True,
        )
        return r.status_code, r.headers['set-cookie']
    except Exception, e:
        return 600, str(e)
