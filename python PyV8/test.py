# encoding:utf8
import PyV8
from lxml import etree
import requests, json


def request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    return etree.HTML(requests.get(url, headers=headers).text)

def toJsonString(object):
    """
    该方法通过使用PyV8库执行JavaScript代码文件，将js对象转换成JSON字符串
    :param object: String,从原HTML文件中爬取到的json对象（当前为字符串）
    :return: object经过转换后的JSON字符串
    """
    with PyV8.JSContext() as ctxt: # 建立一个PyV8的对象
        ctxt.eval(  # 构建完整的JS运行上下文
            u"""
                object = {};
                jsonString = JSON.stringify(object);
            """.format(object) # object为剥离出的 JS 代码
        )
        vars = ctxt.locals # 这句代码的作用查不到，源码没文档，和下边一句代码结合使用吧
        return vars.jsonString  # 将上边那句代码的值转化为 str 并返回

def run(url):
    parseElemet = request(url)
    if parseElemet.xpath('//*[@content="ixigua_pc_detail"]'):  # 如果匹配到视频的页面则不进行爬取
        return
    else:
        # keywords, description = parseElement(parseElemet)
        scriptBlock = list(parseElemet.xpath('//script/text()'))[4][16:]
        scriptBlockJson = toJsonString(scriptBlock)
        scriptBlockDict = json.loads(scriptBlockJson)
        # print(scriptBlockDict)
        # print(scriptBlockJson)

        with open('json.json','w+')as f:
            f.write(scriptBlockJson)

if __name__ == '__main__':
    url = 'https://www.toutiao.com/a6557871064444043779/'
    run(url)