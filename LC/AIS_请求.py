# -*- coding: utf-8 -*
# Time    : 2018/9/6 15:49

import requests
import base64

# mmsi = input('请输入MMSI：')
mmsi = 413488432

param_b = '{mmsi:"'+str(mmsi) + '",ShoreAis:"1"}'
# print(param_b)
# 413488432

param = base64.b64encode(param_b)
# print(param)
# e21tc2k6IjQxMzQ4ODQzMiIsU2hvcmVBaXM6IjEifQ==

sign_key = 'Jhy$xBs5aftk@tDS'
api_key = 'bY@g2fAGRQ$A4C4K'
cmd = '0x5101'
org_id = '0'
uid = 'blmpublic'
upwd = '52bb6b2f09d7095a1c1afec721345817'

version = '0_1.1'


from hashlib import sha1

str_sign = sign_key + 'api_key' + api_key + 'cmd' + cmd + 'org_id' + org_id + 'param' + str(param) + 'uid' + uid + 'upwd' + upwd + 'version'+ version
# str_sign = str(str_sign)
# print(str_sign)
encrypt = sha1()
encrypt.update(str_sign.encode('utf-8'))
sign = encrypt.hexdigest()

# print(sign)
# 1dd1f84f67c5d8c8bdf53d02ef1c7dc5be4b40f2
url = 'http://www.ais.msa.gov.cn/blmcgi?sign='+sign+'&api_key=bY@g2fAGRQ$A4C4K&cmd=0x5101&org_id=0&param='+param+'&uid=blmpublic&version=0_1.1'
r = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': ' zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': ' gzip, deflate',
    'Connection': ' keep-alive',
    'Upgrade-Insecure-Requests': ' 1',
    'Cache-Control': ' max-age=0'
}

data = requests.get(url, params=r)
print(data.text)

# {mmsi:"413488432",time:"1530763503",x:"118.9566",y:"1.4082",cog:"1487",true_head:"319",sog:"4",nav_status:"0",srcid:"100",shipname:"",ship_type:"0",imo:"0",eta:"0",dest:"",destportid:"",draught:"0",length:"0",width:"0",callsign:"",flag:"CHN",match:2,danger:0,sbdlb:""}
