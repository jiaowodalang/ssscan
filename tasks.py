#encoding=utf-8
from celery import Celery
import time
import random
from load_plugin import Load
import os,sys

sys.path.append(os.getcwd())

#app = Celery('tasks', broker='redis://localhost',backend='db+mysql://root:root@127.0.0.1:3306/celery')
app = Celery('tasks', broker='redis://localhost',backend='redis://localhost')

@app.task
def add(x,y):
    
    return x+y



@app.task
def scan(method, url, header, data=None):
    Load(method, url, header, data)
    return True
