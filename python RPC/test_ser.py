import sys
import socketserver
from xmlrpc.server import SimpleXMLRPCServer
import requests

class Server:

    def print1(self):
        print('Hello,print1')

    def print2(self):
        print('Hello,print2')

def music():
    print('music')
    return 'music'

if __name__ == '__main__':
    # ip = sys.argv[1]
    # port = sys.argv[2]
    # ip = ('172.16.101.209')
    # port = '9999'
    #
    # class RPCThreading(socketserver.ThreadingMixIn, SimpleXMLRPCServer):
    #     pass
    #
    # server = Server()
    # ser = RPCThreading(ip, int(port))
    # ser.register_instance(server)
    #
    # print('Listen...')
    # ser.serve_forever()

    address = input("server address : ")

    # A simple server with simple arithmetic functions
    server = SimpleXMLRPCServer((address, 8000), allow_none=True)
    print("Listening on port 8000...")
    server.register_multicall_functions()
    server.register_function(music, 'music')
    server.serve_forever()
