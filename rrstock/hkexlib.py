#-*-coding:utf8-*-
'''
hkex library
'''

### hkex daily quotation list page uri
HKEX_DAYQUOT_LIST_URI = "http://www.hkex.com.hk/eng/stat/smstat/dayquot/qtn.asp"

### hkex daily quotation sepcified by date
### for example: 180125 (d180125e.htm)
HKEX_DAYQUOT_PAGE_URI = "http://www.hkex.com.hk/eng/stat/smstat/dayquot/d%se.htm"

# fields separator in hkex daily quotation
HKEX_DAYQUOT_SEP = "-"*79

HKEX_DAYQUOT_TAB = '''
TABLE OF CONTENT
<a href="#market_highlights">MARKET HIGHLIGHTS</a>
<a href="#quotations">QUOTATIONS</a>
<a href="#sales_all">SALES RECORDS FOR ALL STOCKS</a>
<a href="#sales_over">SALES RECORDS OVER $500,000</a>
<a href="#amendments">AMENDMENT RECORDS FOR TRADE</a>
<a href="#dealings_suspstocks">DEALINGS IN SECURITIES SUSPENDED DUE TO INSUFFICIENT PUBLIC FLOAT</a>
<a href="#adj_turnover">ADJUSTED TURNOVER</a>
<a href="#short_selling">SHORT SELLING TURNOVER - DAILY REPORT</a>
<a href="#adj_short">PREVIOUS DAY'S ADJUSTED SHORT SELLING TURNOVER</a>
<a href="#options_exercised">DETAILS OF OPTION EXERCISED ON 26/01/2018</a>
<a href="#efn_highlights">BOND/NOTES HIGHLIGHTS</a>
<a href="#overseas_highlights">OVERSEAS TURNOVER HIGHLIGHTS</a>
<a href="#other_info">OTHER INFORMATION</a>
'''
