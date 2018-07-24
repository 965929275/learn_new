# encoding:utf8

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['Tricky']

collist = mydb.collection_names()
if "customers" in collist:   # 判断 customers 集合是否存在
    print("集合已存在！")
else:
    print("集合bu存在！")
