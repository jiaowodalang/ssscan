
from tasks import scan
from redisBloom import BloomFilter

def send_scan(method, url, headers, data = None):
    bf = BloomFilter()
    if method == 'GET':
        if bf.isContains(url):
            pass
        else:
            bf.insert(url)
            scan.delay(method, url, headers, data)
    else:
        if type(data) == str and bf.isContains(url+data):
            pass
        else:
            bf.insert(url+data)
            scan.delay(method, url, headers, data)
