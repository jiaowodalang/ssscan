import mitmproxy.http
from mitmproxy import ctx, http
import requests

#from load_plugin import Load
#from tasks import scan
from index import send_scan
from urllib.parse import urlparse

class Joker:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        print(dir(flow.request))
        a = ['constrain_encoding', 'content', 'cookies', 'copy', 'data', 'decode', 'encode', 'first_line_format', 'from_state', 'get_content', 'get_state', 'get_text', 'headers', 'host', 'host_header', 'http_version', 'is_replay', 'make', 'method', 'multipart_form', 'path', 'path_components', 'port', 'pretty_host', 'pretty_url', 'query', 'raw_content', 'replace', 'scheme', 'set_content', 'set_state', 'set_text', 'stream', 'text', 'timestamp_end', 'timestamp_start', 'url', 'urlencoded_form', 'wrap']
        
        print(flow.request.text)
        ctx.log.info("-----------constrain_encoding-----------------")
        print(flow.request.method)
        print(flow.request.url)
        #if flow.request.method == 'POST':
           # r = requests.post(flow.request.url, headers = dict(flow.request.headers), data = flow.request.text)
           # print(r.text)
       # else:
           # r = requests.get(flow.request.url, headers = dict(flow.request.headers))
           # r.encoding='utf8'
            #print(r.text)
        ctx.log.info("-------------content----------------")
        url = urlparse(flow.request.url)
        if url.path.split('.')[-1] not in ['txt','js','jpg','gif','png','woff','css','jpeg','pdf']:
            send_scan(flow.request.method, flow.request.url, dict(flow.request.headers), flow.request.text)
        print(flow.request.headers)
        print(dict(flow.request.headers))
        print(flow.request.raw_content)
        print(dir(flow.request.query))
        print(flow.request.query.keys())
addons = [
    Joker()
]
        
