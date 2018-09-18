# -*- coding: utf-8 -*
# Time    : 2018/9/18 9:43

# encoding:utf-8
# requests 访问后返回的网页的方法
"""
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
'__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__',
'__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__module__', '__ne__',
'__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
'_content','_content_consumed', '_next', 'apparent_encoding', 'close',
'connection'  <requests.adapters.HTTPAdapter object at 0x00000204122254A8>,
'content'  #字节方式的响应体,
'cookies'  网页的cookies,
'elapsed' 相应时间（s）,
'encoding' 网页编码的方式,
'headers' 网页的请求头,
'history', 'is_permanent_redirect',
'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok',
'raise_for_status' <bound method Response.raise_for_status of <Response [200]>>,
'raw'  返回原始响应体，也就是 urllib 的 response 对象,
'reason', 'request',
'status_code' 网页的响应码（200， 403）,
'text' #字符串方式的响应体，会自动根据响应头部的字符编码进行解码,
'url' 网页的请求地址]
"""


# ==============================
# 使用__dict__得到的字符串

"""
{
    '_next': None, 
    'history': [], 
    'request': <PreparedRequest [GET]>, 
    '_content_consumed': True, 
    'status_code': 200, 
    'elapsed': datetime.timedelta(0, 1, 973866), 
    'headers': {'Content-Type': 'text/html; charset=UTF-8', 'CF-RAY': '44e378941ff922e2-LAX', 
    'Expect-CT': 'max-age=604800, 
    report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"', 
    'Server': 'cloudflare', 
    'X-Cache': 'MISS', 
    'Content-Encoding': 'gzip', 
    'Cache-control': 'private', 
    'Set-Cookie': '__cfduid=d074f0f881ddb370ff29b5970947a6cb71534921316; expires=Thu, 22-Aug-19 07:01:56 GMT; path=/; domain=.marinetraffic.com; HttpOnly; Secure, SERVERID=app5; path=/; domain=.marinetraffic.com', 
    'Transfer-Encoding': 'chunked', 
    'Expires': 'Wed, 22 Aug 2018 07:03:56 GMT', 
    'Connection': 'keep-alive', 
    'Date': 'Wed, 22 Aug 2018 07:01:57 GMT', 
    'Strict-Transport-Security': 'max-age=15552000; includeSubDomains'}, 
    '_content': b'<!DOCTYPE html> name="viewport" content="width=device-width, </html>', 
    'url': 'https://www.marinetraffic.com/en/ais/index/search/all/keyword:353693000', 
    'encoding': 'UTF-8', 
    'cookies': <RequestsCookieJar[Cookie(version=0, name='SERVERID', value='app5', port=None, port_specified=False, domain='.marinetraffic.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={}, rfc2109=False), Cookie(version=0, name='__cfduid', value='d074f0f881ddb370ff29b5970947a6cb71534921316', port=None, port_specified=False, domain='.marinetraffic.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=True, expires=1566457316, discard=False, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)]>, 
    'connection': <requests.adapters.HTTPAdapter object at 0x0000022942FE5518>, 
    'raw': <urllib3.response.HTTPResponse object at 0x0000022943246A20>, 
    'reason': 'OK'
}"""


# etree解析后的网页
# html = etree.HTML(page.text)
# page为 request请求的网页原体

"""
['__bool__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', 
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', 
'__setitem__', '__sizeof__', '__str__', '__subclasshook__', '_init', 'addnext', 'addprevious', 
'append', 'attrib', 'base', 'clear', 'cssselect', 'extend', 'find', 'findall', 'findtext', 
'get', 'getchildren', 'getiterator', 'getnext', 'getparent', 'getprevious', 'getroottree', 
'index', 'insert', 'items', 'iter', 'iterancestors', 'iterchildren', 'iterdescendants', 
'iterfind', 'itersiblings', 'itertext', 'keys', 'makeelement', 'nsmap', 'prefix', 'remove', 
'replace', 'set', 'sourceline', 'tag', 'tail', 'text', 'values', 'xpath']
"""