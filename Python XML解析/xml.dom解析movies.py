#encoding:utf8
import xml.dom.minidom
from xml.dom.minidom import parse

# 使用minidom解析器打开XML文档
DOMTree = parse('movies.xml')
# print(DOMTree)
collection = DOMTree.documentElement  #返回文档的根节点
print(collection)
if collection.hasAttribute('shelf'):  # 如果元素具有按名称命名的属性，则返回true 。
    print('Root element: %s' %collection.getAttribute('shelf')) # 以字符串形式返回'shelf'属性的值，如果没有，就返回一个空字符串

# 在集合中获取所有电影
movies = collection.getElementsByTagName('movie') # 返回带有指定标签的对象的集合
print(movies)

for movie in movies:
    print('*****Movie*****')
    if movie.hasAttribute('title'):
        print('Title:',movie.getAttribute('title'))

        type = movie.getElementsByTagName('type')[0]
        # print(type)
        print('type:',type.childNodes[0].data) # 获得元素的子节点集合

        format = movie.getElementsByTagName('format')[0]
        print('format:',format.childNodes[0].data)

        try:
            year = movie.getElementsByTagName('year')[0]
            print('year:', year.childNodes[0].data)
        except:
            pass

        rating = movie.getElementsByTagName('rating')[0]
        print('rating:', rating.childNodes[0].data)

        stars = movie.getElementsByTagName('stars')[0]
        print('stars:', stars.childNodes[0].data)

        description = movie.getElementsByTagName('description')[0]
        print('description:', description.childNodes[0].data)




# # 打印每部电影的详细信息
# for movie in movies:
#    print ("*****Movie*****")
#    if movie.hasAttribute("title"):
#       print ("Title: %s" % movie.getAttribute("title"))

#    type = movie.getElementsByTagName('type')[0]
#    print ("Type: %s" % type.childNodes[0].data)
#    format = movie.getElementsByTagName('format')[0]
#    print ("Format: %s" % format.childNodes[0].data)
#    rating = movie.getElementsByTagName('rating')[0]
#    print ("Rating: %s" % rating.childNodes[0].data)
#    description = movie.getElementsByTagName('description')[0]
#    print ("Description: %s" % description.childNodes[0].data)
