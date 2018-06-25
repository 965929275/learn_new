# XPath基本概念
XPath 是一门在 XML 文档中查找信息的语言。

- XPath 使用路径表达式在 XML 文档中进行导航
- XPath 包含一个标准函数库
- XPath 是 XSLT 中的主要元素
- XPath 是一个 W3C 标准

## XPath路径表达式
XPath 使用路径表达式来选取 XML 文档中的节点或者节点集。这些路径表达式和我们在常规的 **电脑文件系统** 中看到的表达式非常相似。

## XPath节点

### XPath术语

#### 节点
XML 文档是被作为**节点树**来对待的。树的根被称为文档节点或者根节点。

例如此XML文档：
```xml
<?xml version="1.0" encoding="UTF-8"?>

<bookstore>
  <book>
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
</bookstore>
```
其中的节点为：
```xml
<bookstore> (文档节点)

<author>J K. Rowling</author> (元素节点)

lang="en" (属性节点)
```
#### 基本值（原子值）
无父节点或子节点。

eg:
```
J K. Rowling

"en"
```
#### 项目
项目是基本值或者节点。

----
### 节点关系

eg:
```xml
<bookstore>

<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

</bookstore>
```
#### 父节点（Parent）
book 元素是 title、author、year 以及 price 元素的父
#### 子节点（Children）
title、author、year 以及 price 元素都是 book 元素的子
#### 同胞（Sibling）
title、author、year 以及 price 元素都是同胞
#### 先辈（Ancestor）
**所有的父关系**

title 元素的先辈是 book 元素和 bookstore 元素
#### 后代（Descendant）
**所有的子关系**

bookstore 的后代是 book、title、author、year 以及 price 元素

----
## XPath语法
eg:
```xml
<?xml version="1.0" encoding="UTF-8"?>

<bookstore>

<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>
```
### 选取节点
XPath 使用路径表达式在 XML 文档中选取节点。节点是通过沿着路径或者 step 来选取的。 下面列出了最有用的路径表达式：

|表达式  |描述|
|--------|---|
|nodename|选取此节点的所有子节点。|
|/       |从根节点选取。|
|//      |从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。|
|.       |选取当前节点。|
|..      |选取当前节点的父节点。|
|@       |选取属性。|

```python
books_html = etree.HTML(books_data) #从字符串常量中解析出HTML文档
print(type(books_html))  # <class 'lxml.etree._Element'>
print(books_html)  # <Element html at 0x1441cb0cbc8>

result = etree.tostring(books_html) #将元素序列转化为XML的编码字符串表示形式,补全为标准的XML
print(type(result))  # <class 'bytes'>
print(result)
print(result.decode('utf8')) #格式化XML文档

bookstore_all = books_html.xpath('bookstore') #选取bookstore元素的所有子节点
print(bookstore_all) #[]

bookstore = books_html.xpath('/bookstore') #选取根元素bookstore。
# 注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！
print(bookstore) #[]

bookstore_book = books_html.xpath('bookstore/book') # 选取属于bookstore的子元素的所有book元素
print(bookstore_book) #[]

book_all = books_html.xpath('//book') # 选取所有book子元素，忽略位置的影响
print(book_all)
for book in book_all:
    print(book)
    # <Element book at 0x2511707be48 >
    # <Element book at 0x2511707be88 >

bookstore_book_all = books_html.xpath('bookstore//book') # 选取bookstore元素下的所有book元素，忽略位置影响
print(bookstore_book_all) #[]

langs = books_html.xpath('//@lang') # 选取所有名为 lang 的属性
print(langs)  # ['eng', 'eng']
```
### 谓语
谓语用来查找某个特定的节点或者包含某个指定的值的节点。

谓语被嵌在方括号中。

### 选取未知节点
XPath 通配符可用来选取未知的 XML 元素。
|通配符  |描述|
|--------|---|
|*|匹配任何元素节点|
|@*|匹配任何属性节点|
|node()|匹配任何类型节点|

```python
# 选取未知节点
bookstore_alls = books_html.xpath('bookstore/*') # 选取bookstore元素的所有子元素
print('bookstore_alls: %s' %bookstore_alls)

alls = books_html.xpath('//*') # 选取所有元素
print('alls: %s' %alls)
for al in alls:
    print('all: %s' %al)
    print('all: %s' %al.text)

all_titles = books_html.xpath('//title[@*]') # 选取所有带有属性的title元素
print("all_titles: %s" %all_titles)
for title in all_titles:
    print('title: %s' %title.text)
```

### 选取若干路径
在路径表达式中使用"|"运算符，可以选取若干个路径。

```python
# 选取若干路径
book_title_or_price = books_html.xpath('//book/title | //book/price') # 选取book的所有title和price
print('book_title_or_price: %s' %book_title_or_price)
for title_or_price in book_title_or_price:
    print('book_title_or_price: %s' %title_or_price.text)
    # book_title_or_price: Harry Potter
    # book_title_or_price: 29.99
    # book_title_or_price: Learning XML
    # book_title_or_price: 39.95

all_title_or_price = books_html.xpath('//title | //price') # 选取所有title和price
print('all_title_or_price: %s' %all_title_or_price)
for title_or_price in all_title_or_price:
    print('title_or_price： %s' %title_or_price.text)
    # title_or_price： Harry Potter
    # title_or_price： 29.99
    # title_or_price： Learning XML
    # title_or_price： 39.95


bookstore_book_all_title_and_all_price = books_html.xpath('/bookstore/book/title | //price')
# 选取属于bookstore的book的所有title元素和全局所有的price元素
print('bookstore_book_all_title_and_all_price: %s' %bookstore_book_all_title_and_all_price)
```
## XPath轴
轴可定义相对于当前节点的节点集。

![image](https://note.youdao.com/yws/public/resource/a84cb61f17061803a6d37d1450c765de/xmlnote/8BA17AD9C00645419F29434F39B692DD/3004)

## XPath 运算符
XPath 表达式可返回节点集、字符串、逻辑值以及数字。

[菜鸟](http://www.runoob.com/xpath/xpath-operators.html)