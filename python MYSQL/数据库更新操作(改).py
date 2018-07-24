#encoding:utf8
import pymysql

#打开数据库连接
db = pymysql.connect('localhost','root','1234','db_demo1')

# 使用 cursor() 方法获取操作游标
cursor = db.cursor()

#SQL更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE+1 WHERE SEX = '%c'"%('F')
try:
	cursor.execute(sql)
	db.commit()
	print(u'更新成功')
except :
	db.rollback()

db.close()
#此更新将表中性别为“F”的所有“AGE”字段全部加一