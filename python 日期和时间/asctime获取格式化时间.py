# encoding:utf8

import time

ticks = time.time()
localtime = time.localtime(ticks)
asctime = time.asctime(localtime)

print('当前格式化时间：',asctime)