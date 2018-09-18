# -*- coding: utf-8 -*
# Time    : 2018/9/18 9:56

import ftplib

ftp = ftplib.FTP('ftp.sunet.se', 'anonymous', 'anonymous@sunet.se')

# print "File List: "
#
# files = ftp.dir()
#
# print files
print(dir(ftp))
"""
['__doc__', '__init__', '__module__', 
'abort', 'acct', 'af', 'close', 'connect', 'cwd', 'debug', 'debugging', 'delete', 
'dir', 'file', 'getline', 'getmultiline', 'getresp', 'getwelcome', 'host', 'lastresp', 
'login', 'makepasv', 'makeport', 'maxline', 'mkd', 'nlst', 'ntransfercmd', 'passiveserver', 
'port', 'putcmd', 'putline', 'pwd', 'quit', 'rename', 'retrbinary', 'retrlines', 'rmd', 
'sanitize', 'sendcmd', 'sendeprt', 'sendport', 'set_debuglevel', 'set_pasv', 'size', 
'sock', 'storbinary', 'storlines', 'timeout', 'transfercmd', 'voidcmd', 'voidresp', 'welcome']
"""
# ftp.cwd("/pub/unix")