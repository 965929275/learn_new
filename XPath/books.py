from lxml import etree

books_data = """
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
"""

# 选取节点
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


#谓语
bookstore_book_1 = books_html.xpath('/bookstore/book[1]') # 选取属于bookstore子元素的第一个book元素
print(bookstore_book_1)

bookstore_book_last = books_html.xpath('bookstore/book[last()]') # 选取属于bookstore子元素的最后一个book元素
print('bookstore_book_last: %s' % bookstore_book_last)

bookstore_book_last_1 = books_html.xpath('bookstore/book[last()-1]') # 选取属于bookstore子元素的倒数第二个元素book元素
print('bookstore_book_last_1: %s' % bookstore_book_last_1)

bookstore_book_position_3 = books_html.xpath('bookstore/book[position()<3]') # 选取属于bookstore子元素的最前面两个book元素
print('bookstore_book_position_3: %s' % bookstore_book_position_3)

title_lang = books_html.xpath('//title[@lang]') # 选取所有属性为lang的title元素
print("title_lang: %s" % title_lang) #[<Element title at 0x15264562808>, <Element title at 0x15264562848>]
for title in title_lang:
    print("title: %s" %title.text)
    # title: Harry Potter
    # title: Learning XML

title_lang_eng = books_html.xpath('//title[@lang="eng"]') # 选取所有属性lang='eng'的title元素
print("title_lang: %s" % title_lang) #[<Element title at 0x15264562808>, <Element title at 0x15264562848>]
for title in title_lang_eng:
    print("title_eng: %s" %title.text)
    # title_eng: Harry Potter
    # title_eng: Learning XML

bookstore_book_price_above_35 = books_html.xpath('/bookstore/book[price>35.00]') # 选取属于bookstore子元素的所有price>35.00的book元素
print('bookstore_book_price_above_35: %s' %bookstore_book_price_above_35)

bookstore_book_price_above_35_title = books_html.xpath('/bookstore/book[price>35.00]/title') # 选取属于bookstore子元素的所有price>35.00的book元素的title元素
print('bookstore_book_price_above_35_title: %s' %bookstore_book_price_above_35_title)


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