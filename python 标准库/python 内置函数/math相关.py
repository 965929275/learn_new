print(abs(-100))
print(divmod(7, 2))  # 把除数和余数运算结果结合起来,返回元组
a = input()
print(type(a))#根据输入数据判断基本类型
print(pow(2,3))
import math
print(math.pow(2,3))
# 注意：pow() 通过内置的方法直接调用，内置方法会把参数作为整型，而 math 模块则会把参数转换为 float。
print(pow(2, 3, 4))  # pow(x, y[, z]),如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z
print(sum((2, 3, 4), 1))  # 元组计算总和后再加 1
print(sum([0, 1, 2, 3, 4], 2))      # 列表计算总和后再加 2
print(min(1,2,3,4,5))
print(max(1, 2, 3, 4, 5))
