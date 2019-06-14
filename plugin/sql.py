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
from common.sqlmapapi import SQLMAPAPI
from concurrent import futures




info={
    "name":"SQL",
    "level":"HIGH",


}

    
def run(req):

    sqlscan = SQLMAPAPI()
    if req.method == 'GET':
        scan = sqlscan.create_new_task(req.url, req.header)
    elif req.method == 'POST':
        print(req.data)
        scan = sqlscan.create_new_task(req.url, req.header, req.data)
    else:
        scan = None
    if scan == None:
        return
    while sqlscan.get_scan_status() != True:
        time.sleep(3)
    res = sqlscan.get_result()
    if len(res.json()['data']) > 0:
        res.url = req.url
        deal = deal_mysql()
        deal.result(req, res, info)
    return
    
    
