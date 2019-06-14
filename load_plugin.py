#-*- encoding: utf-8 -*-
#main1.py
import os
from concurrent import futures
from urllib.parse import urlparse






module_dir = os.path.dirname(__file__)

path = os.path.join(module_dir, "plugin")
class Load:
    def __init__(self,method,url,header,data=None):
        #self.loadPlugins()
        self.method = method
        self.url = url
        self.getparm = urlparse(url).query.split('&')
        self.header = header
        self.data = data
        self.loadPlugins()

    def loadPlugins(self):
        filenames = []
        tmp = os.listdir(path)
        for filename in tmp:
            if filename.endswith(".py") and not filename.startswith("_"):
                filenames.append(filename)
        print(filenames)
        with futures.ThreadPoolExecutor(max_workers=3) as executor:
            future = [executor.submit(self.runPlugin(filename)) for filename in filenames]
           

    def runPlugin(self, filename):
        pluginName=os.path.splitext(filename)[0]
        plugin=__import__("plugin."+pluginName, fromlist=[pluginName])
        #Errors may be occured. Handle it yourself.
        plugin.run(self)




if __name__=="__main__":
    platform=Load('GET',"http://www.baidu.com",{})
