
from tasks import scan
from redisBloom import BloomFilter

def send_scan(method, url, headers, data = None):
    bf = BloomFilter()
    if bf.isContains(url):
        pass
    else:
        bf.insert(url)
        scan.delay(method, url, headers, data)
    
