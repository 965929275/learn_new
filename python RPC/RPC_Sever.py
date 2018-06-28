from xmlrpc.server import SimpleXMLRPCServer


class MyObject:
    def sayHello(self):
        return "hello xmlprc"

obj = MyObject()
server = SimpleXMLRPCServer(("localhost", 8088))
server.register_instance(obj)

print("Listening on port 8088")
server.serve_forever()