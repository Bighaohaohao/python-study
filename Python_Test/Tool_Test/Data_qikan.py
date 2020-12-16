'''
Author: your name
Date: 2020-12-04 22:10:44
LastEditTime: 2020-12-04 22:25:05
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Tool_Test\Data_qikan.py
'''


import xlrd
import pymysql
#打开数据所在的工作簿，以及选择存有数据的工作表
book = xlrd.open_workbook(r"C:\Users\NICK 豪\Desktop\yzwx(1).xlsx")
sheet = book.sheet_by_name("Sheet2")
#建立一个MySQL连接
conn = pymysql.connect(
        host='localhost', 
        user='root', 
        passwd='123456',  
        db='test',  
        port=3306,  
        charset='utf8'
        )
# 获得游标
cur = conn.cursor()
# 创建插入SQL语句
query = 'insert into qikan_tbl (id,number,name,qikan) values (%s, %s, %s, %s)'
# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
for r in range(1, sheet.nrows):
      id      = sheet.cell(r,1).value
      number       = sheet.cell(r,2).value
      name          = sheet.cell(r,3).value
      qikan     = sheet.cell(r,4).value
      values = (id,number,name,qikan)
      # 执行sql语句
      cur.execute(query, values)
cur.close()
conn.commit()
conn.close()
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print ("导入 " +columns + " 列 " + rows + " 行数据到MySQL数据库!")

# (r"C:\Users\NICK 豪\Desktop\students.xlsx")