# encoding:utf8
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Tricky"]
mycol = mydb["customers"]

mydict = {
    "name":"wangtao",
    "sex":"Men"}

x = mycol.insert_one(mydict)
print(x)