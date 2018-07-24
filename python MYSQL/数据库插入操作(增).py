#encoding:utf8
import pymysql

#打开数据库连接
db = pymysql.connect('localhost','root','1234','db_demo1')

# 使用 cursor() 方法获取操作游标
cursor = db.cursor()

#SQL插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
		VALUES('Mac','Mohan',20,'M',2000)"""
#SQL插入语句的第二种写法:
sql1 = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) \
		VALUES('%s','%s','%d','%c','%d')" % ('Mac1', 'Mohan1', 201, 'M', 20001)
try:
	cursor.execute(sql1)#执行SQL语句
	db.commit()#提交到数据库
	print(u'插入成功')
except:
	db.rollback()#如果发生错误则回滚

db.close()