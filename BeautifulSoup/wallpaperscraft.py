#encoding:utf8
import requests
import os,time
from bs4 import BeautifulSoup


class Wallpapers():
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"}

    def url(self, url):
        html = requests.get(url, headers = self.headers)
        # print(html.text)
        soup = BeautifulSoup(html.text, 'lxml')
        img_download_urls = soup.findAll('a', class_="wallpapers__link")
        hrefs = []
        for url in img_download_urls:
            download = url.get('href')
            href = 'https://wallpaperscraft.com' + download
            hrefs.append(href)
        # print(hrefs)
        self.imageurl(hrefs)

    def imageurl(self, hrefs):
        image_urls = []
        for href in hrefs:
            html = requests.get(href, headers = self.headers)
            soup = BeautifulSoup(html.text, 'lxml')
            img = soup.find('a', class_="JS-Popup")
            src = img.get('href')
            image_urls.append(src)
        self.mkdir('Wallpaper')
        self.save(image_urls)

    def save(self, image_urls):
        print('开始下载')
        for image_url in image_urls:
            name = image_url[41:]
            img = requests.get(image_url)
            with open(name, 'ab') as f:
                f.write(img.content)

    def mkdir(self, path):  # 这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("D:", path))
            os.chdir(os.path.join("D:", path))  # 切换到目录
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False

if __name__ == "__main__":
    n = int(input('请输入要爬取得页数：'))
    for i in range(1, n+1):  # 5731
        time.sleep(5)
        url = 'https://wallpaperscraft.com/all/1920x1080/page'+str(i)
        wall = Wallpapers()
        wall.url(url)
