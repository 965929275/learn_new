#encoding:utf8
#过滤出1~100中平方根是整数的数：
import math
def is_sqr(x):
	return math.sqrt(x) % 1 == 0

newlist = filter(is_sqr, range(1,101))

print(newlist)
print(list(newlist))