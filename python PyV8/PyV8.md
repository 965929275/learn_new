为什么要使用PyV8，这位博主讲解的特别有意思：[使用PyV8在Python爬虫中执行js代码](http://www.php.cn/python-tutorials-352520.html)

质量较高的博文：[使用PyV8解析HTML文档](http://ju.outofmemory.cn/entry/36085)

[简书-Python爬虫:更加优雅的执行JavaScript(PyV8)](https://www.jianshu.com/p/c534d6eb881a)

## 是什么？

>[PyV8](http://code.google.com/p/pyv8/)是一个Python的封装[V8引擎](http://code.google.com/p/v8/)的壳。它提供了简单可用的API，能够利用蟒蛇来构建出的JavaScript的运行时环境。


python的一个包，可以用来执行js代码

## 为什么？

以前用的**requests**、**urllib**等等都是通过浏览器获取**HTML**页面的，HTML相当于一堆文本，爬取数据其实就是通过浏览器响应的HTML解析再得到数据。本质上就是文本处理。

而爬取接口不同于以上内容，爬取接口是获取浏览器的JS代码，我们在本地运行JS代码调取服务器接口，服务器就能将数据直接返回给我们了。

这完全就是两种获取数据的方法啊！！

## 怎么用？

