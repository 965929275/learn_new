# encoding:utf8
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['Tricky']
mycol = mydb['customers']

x = mycol.find()

sort = x.sort('name',-1) # 降序

for i in sort:
    print(i)