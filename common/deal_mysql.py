#! /usr/bin/env python
# coding=utf-8
from urllib.parse import urlparse
import time
import pymysql
import sys
sys.dont_write_bytecode = True

def dealstring(tmp):
    return str(tmp).replace('"','\\\"')

class deal_mysql:
    def __init__(self):
        conn = pymysql.connect(host = '127.0.0.1',port = 3306 , user='root', passwd='',charset='utf8',db='test')
        self.cur = conn.cursor()


    def result(self,req,tmp,info):
        host = urlparse(req.url).netloc
        #print(dealstring(tmp.text))
        sql = 'insert into vuln (host,url,vuln_name,req_header,data,resp_body,resp_header,level,createtime) values("{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(host,tmp.url,info['name'],req.header,dealstring(req.data),dealstring(tmp.text),str(tmp.headers),info['level'],time.time())
        self.cur.execute(sql)



