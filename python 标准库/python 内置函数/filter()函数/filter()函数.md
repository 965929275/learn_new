# filter()函数
## 描述
**filter()** 函数用于过滤掉不符合条件的元素，返回符合条件的新元素。

该函数接受两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或  False，最后将返回 True 的元素放到新的序列当中。

#### 语法
filter(function,iterable)
- function为判断函数
- iterable为可迭代对象

#### 返回值
- python2返回列表
- python3返回filter类

## 实例
```python
#encoding:utf8
#过滤出奇数
def is_odd(n):
	return n % 2 == 1

newlist = filter(is_odd,[1,2,3,4,5,6,7,8,9,10])  #is_odd是判断函数，列表为可迭代对象
print(newlist)#这里返回的是filter类

newlist1 = list(newlist)  #如果想要获取filter类中的数据，可以将其转化为list
print(newlist1)
```
输出：
```
<filter object at 0x000001DFAB1DA5C0>
[1, 3, 5, 7, 9]
```

```python
#encoding:utf8
#过滤出1~100中平方根是整数的数：
import math
def is_sqr(x):
	return math.sqrt(x) % 1 == 0

newlist = filter(is_sqr, range(1,101))

print(newlist)
print(list(newlist))
```
输出：
```
<filter object at 0x000001E467E92F98>
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
----
后记：

filter()函数是一个python的内置函数，在python2中，他返回一个列表，而在python3中，他返回一个可迭代的filter类，这样做的好处是提升了性能，节约了内存。
```python
a = filter(lambda x: x % 2 == 0, range(10))
print(a)
```
输出：
```
<filter object at 0x0000022EC66BB128>
```
这个可迭代的filter()类实现了__iter__和__next__方法, 可以看成是一个迭代器, 有惰性运算的特性。