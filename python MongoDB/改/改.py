# encoding:utf8
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['Tricky']
mycol = mydb['customers']

myquery = {'name': 'wangtao'}

x = mycol.find_one(myquery)
print(type(x))
# print(x['sex'])