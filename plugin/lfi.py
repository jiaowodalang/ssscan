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
    "name":"LFI",
    "level":"MIDDLE",


}

#----------------------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------LFI Scanner--------------------------------------------------------------#
def run(req):
    
    if req.method == 'GET' and req.getparm[0] != '':
        with futures.ThreadPoolExecutor(max_workers=3) as executor:
            future = [executor.submit(scan(req,parm)) for parm in req.getparm]
    
    
    
def scan(req,parm):
    path = os.path.join(os.path.abspath(os.getcwd()), 'dict/lfi.dict')
    with open(path, "r") as f:
        file = f.readlines()
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
            if ("[<a href='function.main'>function.main</a>" not in content
                and "[<a href='function.include'>function.include</a>" not in content
                and ("Failed opening" not in content and "for inclusion" not in content)
                and "failed to open stream:" not in content
                and "open_basedir restriction in effect" not in content
                and ("root:" in content or ("sbin" in content and "nologin" in content)
                or "DB_NAME" in content or "daemon:" in content or "DOCUMENT_ROOT=" in content
                or "PATH=" in content or "HTTP_USER_AGENT" in content or "HTTP_ACCEPT_ENCODING=" in content
                or "users:x" in content or ("GET /" in content and ("HTTP/1.1" in content or "HTTP/1.0" in content))
                or "apache_port=" in content or "cpanel/logs/access" in content or "allow_login_autocomplete" in content
                or "database_prefix=" in content or "emailusersbandwidth" in content or "adminuser=" in content
                or ("error]" in content and "[client" in content and "log" in website)
                or ("[error] [client" in content and "File does not exist:" in content and "proc/self/fd/" in website)
                or ("State: R (running)" in content and ("Tgid:" in content or "TracerPid:" in content or "Uid:" in content)
                    and "/proc/self/status" in website))):
                #print colored("[+] '%s' [Vulnerable]" %website, "red")
                #print "main() [<a href='function.include'>function.include</a>" not in content
                #print "\n------------------------------\n%s\n\n" %content
                #req.url = website
                deal = deal_mysql()
                deal.result(req, r, info)
                break
            else:
                pass
        else:
            pass
    return
