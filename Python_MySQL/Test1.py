# coding:utf-8
import pymysql
import datetime

connection = None
cursor = None
try:
    # 创建数据库连接
    connection = pymysql.connect(host='192.168.16.138',user="root",passwd='123456',db="test")

    # 创建 cursor
    cursor = connection.cursor()

    sql = "select * from user"

    # cursor 执行sql
    try:
        cursor.execute(sql)
        print("-----连接成功-----")

        # 获取cursor执行后的所有结果
        emp = cursor.fetchall()
        print(type(emp))
        print(emp)
    except Exception as ex:
        print(ex)
except Exception as ex:
    print(ex)
finally:
    # 关闭游标和连接
    if cursor:
        cursor.close()
    if connection:
        connection.close()