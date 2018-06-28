# from xmlrpc.client import ServerProxy,MultiCall
from  xmlrpclib import ServerProxy

server = ServerProxy("http://localhost:8088")

url = input("url:")
words = server.run(url)

print ("result:" + words)