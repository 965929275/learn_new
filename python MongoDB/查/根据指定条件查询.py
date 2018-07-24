# encoding:utf8
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['Tricky']
mycol = mydb['customers']

myquery = {'address': 'Valley 345'}

x = mycol.find(myquery)

for i in x:
    print(i)
