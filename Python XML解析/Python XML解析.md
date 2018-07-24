# Python XML解析
## 什么是XML？
XML 指可扩展标记语言（eXtensible Markup Language）。

XML 被设计用来 **传输和存储数据**。

XML是一套定义语义标记的规则，这些标记将文档分成许多部件并对这些部件加以标识。

它也是元标记语言，即定义了用于定义其他与特定领域有关的、语义的、结构化的标记语言的句法语言。

----
## Python对XML的解析
常见的XML编程接口有DOM和SAX

python有三种方法解析XML：SAX，DOM，以及ElementTree:

### 1.SAX (simple API for XML )
python 标准库包含SAX解析器，SAX用事件驱动模型，通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件。
### 2.DOM(Document Object Model)
将XML数据在内存中解析成一个树，通过对树的操作来操作XML。
### 3.ElementTree(元素树)
ElementTree就像一个轻量级的DOM，具有方便友好的API。代码可用性好，速度快，消耗内存少。

注：因DOM需要将XML数据映射到内存中的树，一是比较慢，二是比较耗内存，而SAX流式读取XML文件，比较快，占用内存少，但需要用户实现回调函数（handler）

完整的 SAX API 文档：[Python SAX APIs](https://docs.python.org/3/library/xml.sax.html)

完整的 DOM API 文档：[Python DOM APIs](https://docs.python.org/3/library/xml.dom.html)