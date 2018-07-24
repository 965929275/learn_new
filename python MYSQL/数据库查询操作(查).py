#encoding:utf8
import pymysql

#打开数据库连接
db = pymysql.connect('localhost','root','1234','db_demo1')

# 使用 cursor() 方法获取操作游标
cursor = db.cursor()

#SQL查询语句
sql = "SELECT * FROM EMPLOYEE \
	WHERE INCOME > '%d'" % (10)
try:
	cursor.execute(sql)
	results = cursor.fetchall()# 获取所有记录列表
	for row in results:
		fname = row[0]
		lname = row[1]
		age = row[2]
		sex = row[3]
		income = row[4]
		print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income ))
except:
	print ("Error: unable to fetch data")

db.close()