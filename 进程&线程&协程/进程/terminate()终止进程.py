# encoding:utf8
# 终止一个或多个进程，原因可能是因为进程进入了死循环，或者人为地终止进程
import multiprocessing
import os
import time


def whoami(name):
    print('I am %s, in process %s' %(name, os.getpid()))

def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for num in range(start, stop):
        print('\tNumber %s of %s. Honk!' % (num, stop))
        time.sleep(1)

if __name__ == "__main__":
    whoami('main')
    p = multiprocessing.Process(target=loopy, args=('loopy',))
    p.start()
    time.sleep(5)
    p.terminate()
