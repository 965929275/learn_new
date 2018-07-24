# encoding:utf8
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['Tricky']
mycol = mydb['customers']

x = mycol.delete_many({})

print(x.deleted_count,'个文档已删除')