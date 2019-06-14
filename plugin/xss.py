# LFISuite: LFI Automatic Exploiter and Scanner
# Author: D35m0nd142, <d35m0nd142@gmail.com>
# Twitter: @D35m0nd142
# Python version: 2.7
# Tutorial Video: https://www.youtube.com/watch?v=6sY1Skx8MBc
# Github Repository: https://github.com/D35m0nd142/LFISuite

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import sys
import urllib
#! /usr/bin/env python
# coding=utf-8
#不生成pyc
import sys
sys.dont_write_bytecode = True
import subprocess
import requests
import time
import re
from urllib.parse import urlparse
from common.deal_mysql import deal_mysql
from concurrent import futures



info={
    "name":"XSS",
    "level":"MIDDLE",


}

#----------------------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------LFI Scanner--------------------------------------------------------------#
def run(req):
    
    if req.method == 'GET' and req.getparm[0] != '':
        with futures.ThreadPoolExecutor(max_workers=3) as executor:
            future = [executor.submit(scan(req,parm)) for parm in req.getparm]
    if req.method == 'POST' and req.data != None:
        with futures.ThreadPoolExecutor(max_workers=3) as executor:
            future = [executor.submit(scan(req,parm)) for parm in req.data.split('&')]

    
def scan(req,parm):
    path = os.path.join(os.path.abspath(os.getcwd()), 'dict/xss.dict')
    with open(path,'r') as f:
        file = f.readlines()
    if req.method == 'GET':
        for c in file:
            c = c.strip('\n')
            tmp = parm.split('=')[0]+'='+c
            website = req.url.replace(parm, tmp)
            status_code = 500

            try:
                r = requests.get(website, headers=req.header, timeout=5)
                content = r.text
                status_code = 200
            except:
                pass
                # print "[!] Problem reaching '%s'." %website
                # content = ""

            #content = r.content
            if(status_code == 200):
                if 'Content-Type' in r.headers.keys() and 'application/json' in r.headers['Content-Type']:
                    pass
                elif c in content or re.search('<script>((?!</script>).*?)alert\(/XSSTEST/\)(.*?)</script>', content, flags=0):
                    #req.url = website
                    deal = deal_mysql()
                    deal.result(req, r, info)
                    break
                else:
                    pass
            else:
                pass
        return
    if req.method == 'POST':
        for c in file:
            c = c.strip('\n')
            tmp = parm.split('=')[0]+'='+c
            data = req.data.replace(parm, tmp)
            website = req.url + '?' + data
            status_code = 500

            try:
                r = requests.get(website, headers=req.header, timeout=5)
                content = r.text
                status_code = 200
            except:
                pass
                # print "[!] Problem reaching '%s'." %website
                # content = ""

            #content = r.content
            if(status_code == 200):
                if 'Content-Type' in r.headers.keys() and 'application/json' in r.headers['Content-Type']:
                    pass
                elif c in content or re.search('<script>((?!</script>).*?)alert\(/XSSTEST/\)(.*?)</script>', content, flags=0):
                    #req.url = website
                    deal = deal_mysql()
                    deal.result(req, r, info)
                    break
                else:
                    pass
            else:
                pass
        return
