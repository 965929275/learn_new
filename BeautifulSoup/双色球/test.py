import urllib.request
URL = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
htmlContent = urllib.request.urlopen(URL)
print(htmlContent)
