from .dbmlib import (
    SqliteHandler,
    STOCK_LIST_TPL,
    STOCK_DATA_TPL,
)

from .utillib import (
    genTs,
    chomp,
    http_get,
    set_cookie,
    se_convert,
    shell_exec,
    time_now_fmt,
    time_now_its,
    UriTemplate,
    genUrlByTemplate,
)

from .envlib import *

from .hkexlib import *

from xqlib import *

HTTP_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
    'Content-type': 'application/x-www-form-urlencoded',
}

#def set_xq_cookie():
#    return set_cookie(XQ_HOMEPAGE_URI, HTTP_HEADERS)

def set_xq_header():
    XQ_HTTP_HEADERS = HTTP_HEADERS
    status, cookie = set_cookie(XQ_HOMEPAGE_URI, XQ_HTTP_HEADERS)
    if status == 200: XQ_HTTP_HEADERS['cookie'] = cookie
    return XQ_HTTP_HEADERS
