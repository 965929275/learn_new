# encoding:utf8
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['Tricky']
mycol = mydb['customers']

myquery = {'address': 'Sky st 331'}

mycol.delete_one(myquery)

for i in mycol.find():
    print(i)