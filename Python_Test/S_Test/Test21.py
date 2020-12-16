'''
Author: your name
Date: 2020-11-18 16:54:09
LastEditTime: 2020-11-20 15:35:12
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Test21.py
'''
# 使用__slots__限制修改对象的属性，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Student(object):
    __slots__ =("name","age") 
stu=Student()
stu.name="john"
stu.age=20
# 无法修改对象属性
# sru.sex="man"