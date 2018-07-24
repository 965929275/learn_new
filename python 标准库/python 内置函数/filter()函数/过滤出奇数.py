#encoding:utf8
#过滤出奇数
def is_odd(n):
	return n % 2 == 1

newlist = filter(is_odd,[1,2,3,4,5,6,7,8,9,10])  #is_odd是判断函数，列表为可迭代对象
print(newlist)#这里返回的是filter类

newlist1 = list(newlist)  #如果想要获取filter类中的数据，可以将其转化为list
print(newlist1)