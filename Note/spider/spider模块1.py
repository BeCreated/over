# -*- coding: utf-8 -*
# Time    : 2018/9/18 9:49
import requests


class Spider:
    def __init__(self, url=None, dl_ip=None):
        self.url = url
        self.dl_ip = dl_ip

    def spider_headers(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/53.0.2785.89 Safari/537.36'
        }
        return headers

    def spider_url(self):
        headers = self.spider_headers()
        proxy = self.dl_ip
        if proxy is None:
            request_s = requests.get(self.url, headers=headers, )
        else:
            request_s = requests.get(self.url, headers=headers, proxies=proxy)
        # content_html = request_s.text.encode('latin1').decode('utf8')
        # content_html = request_s.text.encode('latin1').decode('gbk')
        # content_html = request_s.text.encode('gbk').decode('utf8')
        content_html = request_s.text
        return content_html
