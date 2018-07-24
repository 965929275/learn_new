# encoding:utf8
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['Tricky']
mycol = mydb['customers']

# 读取 address 字段中第一个字母 ASCII 值大于 "S" 的数据，大于的**修饰符**条件为 {"$gt": "S"}:
myquery = {'address': {'$gt': 'S'}}

x = mycol.find(myquery)

for i in x:
    print(i)

# 读取 address 字段中第一个字母为 "S" 的数据，**正则表达式**为 {"$regex": "^S"} :
myquery_re = {'address': {'$regex': '^S'}}

y = mycol.find(myquery_re)

for i in y:
    print(i)
