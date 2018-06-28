import time
from xmlrpc.client import ServerProxy,MultiCall

def run():
    # server = ServerProxy('172.16.101.209')
    # rstr = server.get('username', url)
    address = input("server address : ")
    proxy = ServerProxy(address, 8000, allow_none=True)
    multicall = MultiCall(proxy)
    multicall.music()

if __name__ == '__main__':
    # url = 'https://www.baidu.com/'
    run()