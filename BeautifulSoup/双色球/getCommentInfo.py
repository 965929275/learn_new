#encoding:utf8
import re
import urllib.request
from bs4 import BeautifulSoup
from mylog import MyLog as mylog


class DoubleColorBallItem(object):
    date = None
    order = None
    read1 = None
    read2 = None
    read3 = None
    read4 = None
    read5 = None
    read6 = None
    blue = None
    Money = None
    firstPrize = None
    secondPrize = None

class GetDoubleColorBallNumber(object):
    def __init__(self):
        self.urls = []
        # print(self.urls)
        self.log = mylog()
        self.getUrls()
        self.items = self.spider(self.urls)
        self.piplines(self.items)
        # print(self.urls)

    def getUrls(self):
        URL = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
        htmlContent = self.getResponseContent(URL)
        # print(htmlContent)
        soup = BeautifulSoup(htmlContent,'lxml')
        tag = soup.find_all(re.compile('p'))[-1]
        print(tag)
        pages = tag.strong.get_text()
        for i in range(1,2):#int(pages)+1):
            url = r'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%d.html' %i
            self.urls.append(url)
            # print(self.urls)
            self.log.info(u'添加URL：%s 到URLS \r\n' %url)

    def getResponseContent(self,url):
        try:
            response = urllib.request.urlopen(url)
            # print(response)
        except:
            self.log.error(u'python返回URL：%s 数据失败 \r\n' %url)
        else:
            self.log.info(u'python返回：%s 数据成功 \r\n' %url)
            return response.read()

    def spider(self,urls):
        items = []
        for url in urls:
            htmlContent = self.getResponseContent(url)
            soup = BeautifulSoup(htmlContent,'lxml')
            tags = soup.find_all('tr',attrs={})
            for tag in tags:
                if tag.find('em'):
                    item = DoubleColorBallItem()
                    tagTd = tag.find_all('td')
                    # print(tagTd[3].get_text())
                    item.date = tagTd[0].get_text()
                    item.order = tagTd[1].get_text()
                    tagEm = tagTd[2].find_all('em')
                    item.read1 = tagEm[0].get_text()
                    item.read2 = tagEm[1].get_text()
                    item.read3 = tagEm[2].get_text()
                    item.read4 = tagEm[3].get_text()
                    item.read5 = tagEm[4].get_text()
                    item.read6 = tagEm[5].get_text()
                    item.blue = tagEm[6].get_text()
                    item.Money = tagTd[3].get_text()
                    item.firstPrize = tagTd[4].find('strong').get_text()
                    item.secondPrize = tagTd[5].find('strong').get_text()
                    items.append(item)
        return items

    def piplines(self,items):
        fileName = u'双色球.txt'
        with open(fileName,'w',encoding='utf8') as f:
            for item in items:
                f.write('%s %s \t %s %s %s %s %s %s %s \t %s \t %s %s \n'
                %(item.date,item.order,item.read1,item.read2,item.read3,item.read4,item.read5,item.read6,
                item.blue,item.Money,item.firstPrize,item.secondPrize))
                self.log.info(u'将日期为：%s的数据存入到“%s”'%(item.date,fileName))


if __name__ == '__main__':
    GDCBN = GetDoubleColorBallNumber()




