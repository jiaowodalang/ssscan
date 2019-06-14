
# -*- coding:utf-8 -*-
# wirter:En_dust
import requests
import json
import time

class SQLMAPAPI():
    def __init__(self,server_ip = '127.0.0.1',server_port = '8775'):
        self.server = "http://" + server_ip + ":" + server_port
        self.status = ""
        self.header = {'Content-Type': 'application/json'}
        # self.taskid = json.loads(requests.get("%s/task/new" % self.server).text)['taskid']


    def set_task_options(self,headers):
        
        sqlmap_conf={}
        sqlmap_conf['headers'] = ''
        for header in headers.keys():
            sqlmap_conf['headers'] += "%s: %s\r\n" % (header, headers[header])
        try:
            requests.post("%s/option/%s/set" % (self.server, self.taskid), data=json.dumps(sqlmap_conf), headers=self.header)
        except:
            pass



    def start_target_scan(self, url, headers, data):
        '''开始扫描的方法,成功开启扫描返回True，开始扫描失败返回False'''
        self.set_task_options(headers)
        r = requests.post(self.server + '/scan/' + self.taskid + '/start',
                      data=json.dumps({'url':url,'data':data}),
                      headers=self.header)
        if r.json()['success']:
            return r.json()['engineid']
        else:
            #print(r.json())
            return None

    def get_scan_status(self):
        '''获取扫描状态的方法,扫描完成返回True，正在扫描返回False'''
        self.status = json.loads(requests.get(self.server + '/scan/' + self.taskid + '/status').text)['status']
        if self.status == 'terminated':
            return True
        elif self.status == 'running':
            #print("Running")
            return False
        else:
            #print("未知错误！")
            self.status = False
    


    def get_result(self):
        '''获取扫描结果的方法，存在SQL注入返回payload和注入类型等，不存在SQL注入返回空'''
        if(self.status):
            r = requests.get(self.server + '/scan/' + self.taskid + '/data')
            return r
    def create_new_task(self, url, headers, data=''):
        '''创建一个新的任务，创建成功返回taskid'''
        try:
            r = requests.get("%s/task/new"%(self.server),timeout=5)
            self.taskid = r.json()['taskid']
            if self.taskid != "":
                task = self.start_target_scan(url, headers, data)
                if task:
                    return True
                else:
                    return None
            else:
                print("创建任务失败!")
                return None
        except:
            return None
if __name__ == '__main__':
    a = SQLMAPAPI()
    b = {'user-agernt':'curl'}
    a.create_new_task('http://www.baidu.com?a=1',b)
