# encoding:utf8

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27010/')
mydb = myclient["Tricky"]