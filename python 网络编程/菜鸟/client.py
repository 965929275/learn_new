# encoding:utf8
# 客户端
import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

# 连接服务，指定主机和端口
# 打开一个 TCP 连接到主机为 hostname 端口为 port 的服务商
s.connect((host,port))

# 接收小于 1024 字节的数据
msg = s.recv(1024)

# 操作完成后要关闭连接
s.close()

print(msg.decode('utf-8'))
