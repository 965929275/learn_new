# encoding:utf8
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['Tricky']
mycol = mydb['customers']

myquery = {"address": {"$regex": "^S"}}

for i in mycol.find(myquery):
    print(i)

x = mycol.delete_many(myquery)

print(x.deleted_count,'个文件已删除')
