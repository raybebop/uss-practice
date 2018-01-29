#-*-coding:utf8-*-

import os, sys, re

HKEX_HOMEPAGE = "http://www.hkex.com.hk"
HKEX_DAYQUOT_LIST = "http://www.hkex.com.hk/eng/stat/smstat/dayquot/qtn.asp"

# daily quotation sepcified by date
# for example: 180125 (d180125e.htm)
HKEX_DAYQUOT_TPL = "http://www.hkex.com.hk/eng/stat/smstat/dayquot/d%se.htm"

# fields separator in daily quotation
HKEX_DAYQUOT_SEP = "-"*79
