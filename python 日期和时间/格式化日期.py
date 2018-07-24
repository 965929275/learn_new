# encoding:utf8

import time

# 格式化成 2018-06-12 11:19:06 的形式
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# 格式化成 Tue Jun 12 11:23:07 的形式
print(time.strftime('%a %b %d %H:%M:%S', time.localtime()))

# 将格式化字符串转化为时间戳
a = 'Tue Jun 12 11:23:07 2018'
print(time.mktime(time.strptime(a, '%a %b %d %H:%M:%S %Y')))

b = '2018-06-12 11:27:44'
print(time.mktime(time.strptime(b, '%Y-%m-%d %H:%M:%S')))
