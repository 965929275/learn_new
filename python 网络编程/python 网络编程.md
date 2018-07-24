# python 网络编程

Python 提供了两个级别访问的网络服务。：

- 低级别的网络服务支持基本的 Socket，它提供了标准的 BSD Sockets API，可以访问底层操作系统Socket接口的全部方法。
- 高级别的网络服务模块 SocketServer， 它提供了服务器中心类，可以简化网络服务器的开发。

## Socket

“套接字”，向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。 

## 服务器端（server）

1. 创建socket对象 **serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)**
2. 获取本地主机名 **gethostname()**
3. 设置端口号 **port = 9999**
4. 绑定端口号 **serversocket.bind((host, port))**
5. 建立客户端连接

## 客户端（client）

1. 创建socket对象 **s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)**
2. 获取本地主机名 **gethostname()**
3. 设置端口号 **port = 9999**
4. 连接服务，指定主机和端口 **s.connect((host, port))**
5. 接收数据
6. 关闭连接


## ps

每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户端了。 

网络通信是两个进程之间的通信。