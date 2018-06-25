# encoding:utf8
from lxml import etree
import requests
# from pymongo import MongoClient
# 我尼玛呀，用了一上午就爬出来个 title，半天才发现，页面返回的 js 代码，所以这种情况才要用 PyV8 啊，填坑了，填坑了。。。

class TouTiaoSpider(object):
    
    # def __init__(self, article_list):
    #     self.artcile_list = article_list
    #     self.conn = MongoClient('localhost', 27017)

    def request(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        # print str(etree.HTML(requests.get(url, headers=headers).text))
        return etree.HTML(requests.get(url, headers=headers).text)

    def spider(self):
        parseElement = self.request(url)
        title = parseElement.xpath('//title')[0].text
        print(title)
        meta = parseElement.xpath('//meta')
        for mr in meta:
            print mr.text

if __name__ == '__main__':
    url = 'https://www.toutiao.com/a6569571907211887112/'
    spider = TouTiaoSpider()
    spider.spider()