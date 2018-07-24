# 1. 安装MySQL模块：
`pip install PyMySQL`
# 2. 数据库连接：
```python
import pymysql

#打开数据库连接
db = pymysql.connect('localhost','root','1234','db_demo1')#host,用户名，密码，数据库名

#使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

#使用execute()方法执行SQL查询
cursor.execute('SELECT VERSION()')

#使用fetchone()方法获取单条数据
data = cursor.fetchone()

print ('Database version: %s'%data)
```
运行结果：
`Database version: 5.7.20`
# 3. 创建数据库表：
```python
#encoding:utf8
import pymysql

#打开数据库连接
db = pymysql.connect('localhost','root','1234','db_demo1')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')#EMPLOYEE是表名

#使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
    FIRST_NAME  CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT)"""

cursor.execute(sql)
print(u'创建成功')

#关闭数据库
db.close()
```
# 4. 增：
```python
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
```
# 5. 删：
```python
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
```
# 6. 改：
```python
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
```
# 7. 查：
```python
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
```
# 8. 执行事务
> 事务机制可以确保数据一致性。
>
>事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。
>
>- 原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
>
>- 一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
>
>- 隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
>
>- 持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。
>
>Python DB API 2.0 的事务提供了两个方法 `commit` 或 `rollback`。
>
>*--摘自菜鸟教程*

我理解为即使某个SQL语句所在的模块出错也不影响整个编程环境的状态。

