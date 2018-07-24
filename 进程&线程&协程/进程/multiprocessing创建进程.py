#encoding:utf8
import multiprocessing
import os
import time


def do_this(what):
    whoami(what)


def whoami(what):
    print('Process %s says: %s' % (os.getpid(), what))


if __name__ == "__main__":
    whoami('I am the main program.')
    for n in range(4):
        time.sleep(1)
        # Process创建了一个进程用来执行do_this()函数
        p = multiprocessing.Process(
            target=do_this, args=('I am function %s' % n,))
        p.start()
        p.join() # join()方法可以等待子进程结束后再继续往下执行，通常用于进程间的同步。
