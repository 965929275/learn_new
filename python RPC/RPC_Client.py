from xmlrpc.client import ServerProxy,MultiCall

server = ServerProxy("http://localhost:8088")

words = server.sayHello()

print ("result:" + words)