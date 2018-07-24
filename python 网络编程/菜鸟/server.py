# encoding:utf8
# 服务器端
import socket, sys

# 创建socket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
print(host)
port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    # 等待客户端的连接，返回connection对象，表示已连接客户端。
    clientsocket,addr = serversocket.accept()

    print('连接地址：%s' % str(addr))
    
    msg = '连接成功' + '\r\n'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()