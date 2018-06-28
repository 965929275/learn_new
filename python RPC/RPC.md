## RPC

简单，易理解：[Python 中使用 XMLRPC（入门）](https://www.cnblogs.com/lxt287994374/p/3904219.html)

在flask中使用：[python 简单 RPC 示例](https://www.jianshu.com/p/40af791a7b1e)

> ## 定义
>
> **远程过程调用**（Remote Procedure Call ），是一个计算机通信[协议](https://zh.wikipedia.org/wiki/%E7%B6%B2%E7%B5%A1%E5%82%B3%E8%BC%B8%E5%8D%94%E8%AD%B0)。该协议允许运行于一台计算机的[程序](https://zh.wikipedia.org/wiki/%E7%A8%8B%E5%BA%8F)调用另一台计算机的[子程序](https://zh.wikipedia.org/wiki/%E5%AD%90%E7%A8%8B%E5%BA%8F)，而程序员无需额外地为这个交互作用编程。如果涉及的软件采用[面向对象编程](https://zh.wikipedia.org/wiki/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%BC%96%E7%A8%8B)，那么远程过程调用亦可称作**远程调用**或**远程方法调用**，例：[Java RMI](https://zh.wikipedia.org/wiki/Java_RMI)。 
>
> ## 信息传递
>
> 远程过程调用是一个[分布式计算](https://zh.wikipedia.org/wiki/%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97)的[客户端 - 服务器](https://zh.wikipedia.org/wiki/%E5%AE%A2%E6%88%B7%E7%AB%AF-%E6%9C%8D%E5%8A%A1%E5%99%A8)（Client/Server）的例子，它简单而又广受欢迎。远程过程调用总是由[客户端](https://zh.wikipedia.org/wiki/%E5%AE%A2%E6%88%B7%E7%AB%AF)对[服务器](https://zh.wikipedia.org/wiki/%E6%9C%8D%E5%8A%A1%E5%99%A8)发出一个执行若干过程请求，并用客户端提供的参数。执行结果将返回给客户端。由于存在各式各样的变体和细节差异，对应地派生了各式远程过程调用协议，而且它们并不互相兼容。
>
> ——维基百科

以下内容转自[Python 中使用 XMLRPC（入门）](https://www.cnblogs.com/lxt287994374/p/3904219.html)，博主写的很好，就直接保存下来了。

## 一、简介

　　RPC 是 Remote Procedure Call 的缩写，翻译成中文为：远程方法调用。

它是一种在本地机器上调用远端机器上的一个过程（方法）的技术，这个过程也被大家称为 “分布式计算”，是为了提高各个分立机器的 “互操作性” 而发明出来的技术。

　　XML-RPC 的全称是 XML Remote Procedure Call，即 XML 远程方法调用。

它是一套允许运行在不同操作系统、不同环境的程序实现基于 Internet 过程调用的规范和一系列的实现。这种远程过程调用使用 http 作为传输协议，XML 作为传送信息的编码格式。Xml-Rpc 的定义尽可能的保持了简单，但同时能够传送、处理、返回复杂的数据结构。XML- RPC（[http://www.xmlrpc.com](http://www.xmlrpc.com/)）是由美国 UserLand 公司指定的一个 RPC 协议。简单的理解是：将数据定义为 xml 格式，通过 http 协议进行远程传输。

## 二、优点

1. 传输复杂的数据。
2. 通过程序语言的封装，实现远程对象的调用。

###  三、Python 下的 XML-RPC

1. 类库：SimpleXMLRPCServer

　　一般使用在服务器端，这个模块用来构造一个最基本的 XML-RPC 服务器框架。

2. 类库：xmlrpclib

　　一般使用在客户端，这个模块用来调用注册在 XML-RPC 服务器端的函数，xmlrpclib 并不是一个类型安全的模块，无法抵御恶意构造的数据，这方面的一些处理工作需要交给开发者自己。

 

大致用法：使用 SimpleXMLRPCServer 模块运行 XMLRPC 服务器，在其中注册服务器提供的函数或者对象；然后在客户端内使用 xmlrpclib.ServerProxy 连接到服务器，想要调用服务器的函数，直接调用 ServerProxy 即可。

 

简单实例：hello xmlprc

服务器端：xmlrpc_server.py

```python
import SimpleXMLRPCServer

class MyObject:
    def sayHello(self):
        return "hello xmlprc"

obj = MyObject()
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8088))
server.register_instance(obj)

print "Listening on port 8088"
server.serve_forever()
```

 

客户端：xmlrpc_client.py

```python
import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:8088")

words = server.sayHello()

print "result:" + words
```

  打开一个终端，输入命令，运行服务器端程序：


chmod u+x xmlrpc_server.py
python xmlrpc_server.py

打开另一个新的终端，输入命令，运行客户端程序：


chmod u+x xmlrpc_client.py
python xmlrpc_client.py

可以看到客户端控制台上输出了：hello xmlprc。如图：

![](https://images0.cnblogs.com/i/470415/201408/111028435308942.png)



SimpleXMLRPCServer是一个单线程的服务器。这意味着，如果几个客户端同时发出多个请求，其它的请求就必须等待第一个请求完成以后才能继续。
若修改服务器端如下：

```python
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SocketServer import ThreadingMixIn
class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):pass

class MyObject:
    def sayHello(self):
        return "hello xmlprc"

obj = MyObject()
server = ThreadXMLRPCServer(("localhost", 8088), allow_none=True)
server.register_instance(obj)

print "Listening on port 8088"
server.serve_forever()
```

　此时，服务器就支持多线程并发了。

----

#### PS:

我理解RPC与分布式有关系了，当启用多线程，多进程，高并发时，它又与消息队列有关了。

