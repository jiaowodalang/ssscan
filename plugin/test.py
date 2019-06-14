#! /usr/bin/env python
# coding=utf-8







#不生成pyc
import sys
sys.dont_write_bytecode = True
#sys.path.append("..")



import requests
import time
import re
from urllib.parse import urlparse
from common.deal_mysql import deal_mysql


#import pymysql
#conn = pymysql.connect(host = '127.0.0.1',port = 3306 , user='root', passwd='',charset='utf8',db='test')
#cur = conn.cursor()


info={ 
    "name":"personal message info",
    "level":"INFO",


}





def stringIsPhone(string):
    iphones = re.findall(
            r'[%"\'< ](?:13[012]\d{8}[%"\'< ]|15[56]\d{8}[%"\'< ]|18[56]\d{8}[%"\'< ]|176\d{8}[%"\'< ]|145\d{8}[%"\'< ]|13[456789]\d{8}[%"\'< ]|147\d{8}[%"\'< ]|178\d{8}[%"\'< ]|15[012789]\d{8}[%"\'< ]|18[23478]\d{8}[%"\'< ]|133\d{8}[%"\'< ]|153\d{8}[%"\'< ]|189\d{8}[%"\'< ])', string)
    if iphones != []:
        iphones = set(iphones)
        return iphones
    return False

def stringIsIdCard(string):
    coefficient = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    parityBit = '10X98765432'
    idcards = re.findall(r'([1-8][1-7]\d{4}[1|2]\d{3}[0|1]\d{1}[1-3]\d{4}[0-9|X|x])', string)
    if idcards != []:
        for idcard in idcards:
            sumnumber = 0
            for i in range(17):
                sumnumber += int(idcard[i]) * coefficient[i]
            if parityBit[sumnumber % 11] == idcard[-1]:
                return True

    return False


def run(req):
    #host = urlparse(req.url).netloc
    if req.method == 'GET':
        try:
            tmp = requests.get(req.url, headers = req.header, timeout=5)
        
            tmp.encoding = 'utf-8'
            res = stringIsPhone(str(tmp.content))
            res2 = stringIsIdCard(tmp.text)
            if res or res2:
                deal = deal_mysql()
                deal.result(req,tmp,info)
        except:
            pass
        
    if req.method == 'POST':
        try:
            tmp = requests.post(req.url, headers = req.header, data = req.data, timeout=5)
            tmp.encoding = 'utf-8'
            res = stringIsPhone(str(tmp.content))
            res2 = stringIsIdCard(tmp.text)
            if res or res2:
                deal = deal_mysql()
                deal.result(req,tmp,info)
        except:
            pass
