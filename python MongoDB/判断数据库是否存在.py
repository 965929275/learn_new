# encoding:utf8
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

dblist = myclient.database_names()
if 'Tricky' in dblist:
    print('Tricky数据库已存在')