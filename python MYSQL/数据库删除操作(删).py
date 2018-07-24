#encoding:utf8
import pymysql

#打开数据库连接
db = pymysql.connect('localhost','root','1234','db_demo1')

# 使用 cursor() 方法获取操作游标
cursor = db.cursor()

#SQL数据库删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (200)
try:
	cursor.execute(sql)
	db.commit()
	print(u'删除成功')
except:
	db.rollback()

db.close()