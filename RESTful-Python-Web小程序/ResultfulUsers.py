# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import Flask, jsonify
from flask import abort
from flask import make_response
import pymysql

class Mysql(object):

    def __init__(self, id, name):
        self.name = name
        self.id = id

     #数据库插入
    def InsertSql(self):

        #连接数据库
        db = pymysql.connect("localhost", "root", "123456", "pythondb")

        #获得操作游标
        cursor = db.cursor()
        sql1 = "INSERT INTO USER (ID,NAME)VALUES(%s, %s)"
        try:

            #执行数据库语句
           cursor.execute(sql1, (self.id, self.name))

           #提交操作
           db.commit()

        except:
           db.rolback()
        db.close()


    def SelectSql(self):
        db = pymysql.connect("localhost", "root", "123456", "pythondb")
        cursor = db.cursor()
        sql2 = "SELECT * FROM USER WHERE ID = %s"
        try:
            cursor.execute(sql2, self.id)

            #获取查询的结果（一行元组，一条记录  tuple）
            result = cursor.fetchone()
        except:
            db.rollback()
        db.close()

        #将结果返回给调用它的函数
        return result

    def SelectAllSql(self):
        db = pymysql.connect("localhost", "root", "123456", "pythondb")
        cursor = db.cursor()
        sql2 = "SELECT * FROM USER"
        try:
            cursor.execute(sql2)

            #获取查询结果（二维元组，元组中含元组， 多条记录， tuple）
            results = cursor.fetchall()
        except :
            db.rollback()
        db.close()
        return results

    def UpdateSql(self):
        db = pymysql.connect("localhost", "root", "123456", "pythondb")
        cursor = db.cursor()
        sql3 = "UPDATE USER SET NAME = %s WHERE ID = %s"
        try:
            cursor.execute(sql3, (self.name, self.id))
            db.commit()
        except:
            db.rollback()
        db.close()

    def DeleteSql(self):
        db = pymysql.connect("localhost", "root", "123456", "pythondb")
        cursor = db.cursor()
        sql4 = "DELETE FROM USER WHERE ID = %s"
        try:
            cursor.execute(sql4, self.id)
            db.commit()
        except:
            db.rollback()
        db.close()

class Web(object):
    app = Flask(__name__)

    @app.route('/users', methods=['GET'])
    def get_users():

        #调用Mysql类并传递参数
        SeAllSql = Mysql("", "")

        #调用Mysql类中的SelectAllSql函数并接收返回结果（返回的格式是元组）
        AllUser_Message = SeAllSql.SelectAllSql()

        #将接收到的数据以jsonify格式传给网页
        return jsonify(AllUser_Message)

    @app.route('/users/<user_id>', methods=['GET'])
    def get_user(user_id):
        id = user_id
        print(id)
        SeSql = Mysql(id, "")

        #接收到的结果是一元组 tuple
        User_Message = SeSql.SelectSql()

        #将获取一元组的内容，并将其分别以json格式传给网页
        return jsonify({'id': User_Message[0], 'name': User_Message[1]})

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    @app.route('/users', methods=['post'])
    def create_user():

        #获得请求body中的数据
        id = request.json.get('id')
        name = request.json.get('name')
        InSql = Mysql(id, name)
        InSql.InsertSql()
        return jsonify('OK'), 201

    @app.route('/users/<user_id>', methods=['put'])
    def update_user(user_id):
        id = user_id
        name = request.json.get('name')
        UpSql = Mysql(id, name)
        UpSql.UpdateSql()
        return jsonify("OK")

    @app.route('/users/<user_id>', methods=['DELETE'])
    def delete_user(user_id):
        id = user_id
        DeSql = Mysql(id, "")
        DeSql.DeleteSql()
        return jsonify("OK")


if __name__ == '__main__':
    Web.app.run(debug=True)








