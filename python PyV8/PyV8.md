为什么要使用PyV8，这位博主讲解的特别有意思：[使用PyV8在Python爬虫中执行js代码](http://www.php.cn/python-tutorials-352520.html)

质量较高的博文：[使用PyV8解析HTML文档](https://www.h5jun.com/post/PyV8.html)（这篇博文里的代码有问题，也没有说明是py2，还是py3，看着一大堆代码，还以为很高级，放弃了(′д｀ )…彡…彡）

人家用的py2.。换了一下环境直接就好了。。。

去他大爷的，还是不能用，浪费老子时间。。。

[简书-Python爬虫:更加优雅的执行JavaScript(PyV8)](https://www.jianshu.com/p/c534d6eb881a)

## 是什么？

>[PyV8](http://code.google.com/p/pyv8/)是一个Python的封装[V8引擎](http://code.google.com/p/v8/)的壳。它提供了简单可用的API，能够利用蟒蛇来构建出的JavaScript的运行时环境。


python的一个包，可以用来执行js代码

## 为什么？

以前用的**requests**、**urllib**等等都是通过浏览器获取**HTML**页面的，HTML相当于一堆文本，爬取数据其实就是通过浏览器响应的HTML解析再得到数据。本质上就是文本处理。

而爬取接口不同于以上内容，爬取接口是获取浏览器的JS代码，我们在本地运行JS代码调取服务器接口，服务器就能将数据直接返回给我们了。

这完全就是两种获取数据的方法啊！！

----

爬今日头条文章内容的时候发现页面就是直接返回的js代码，数据就嵌在js代码里，执行了js代码后，就能返回Json数据了，这种情况也要用到PyV8.

## 怎么用？

*以下都是心血，是精华啊*

1. 得到页面的源代码后，将页面内的`<script>...</script>`标签内的**JS**代码剥离出来
2. 将**JS**代码中的`var BASE_DATA = {...};`代码剥离出来，这里面装的就是我们想要得数据
3. 再将`var BASE_DATA = {...};`中的`...`剥离出来
4. 建立一个PyV8的对象
5. 为剥离出的`...`构建完整的**JS**运行上下文
6. `PyV8.eval()`函数执行构建好的**JS**代码
7. 返回 **str**类型的数据

```python
with PyV8.JSContext() as ctxt:  # 建立一个PyV8的对象
    ctxt.eval(  #  构建完整的JS运行上下文
        u"""
                object = {};
                jsonString = JSON.stringify(object);
            """.format(object)  # object为剥离出的 JS 代码
    )
    vars = ctxt.locals  #这句代码的作用查不到，源码没文档，和下边一句代码结合使用吧
    return vars.jsonString  #将上边那句代码的值转化为 str 并返回
```

