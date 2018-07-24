# encoding:utf8
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['Tricky']
mycol = mydb['customers']

x = mycol.find({}, {'_id': 0, 'name': 1, 'address': 1})

for i in x:
    print(i)