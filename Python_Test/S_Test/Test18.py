'''
Author: your name
Date: 2020-11-17 14:10:22
LastEditTime: 2020-11-17 14:23:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Test18.py
'''
# 为对象动态添加属性
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
p = Person("张三",20)
print(p)
p.sex = 'male'
print(p.sex)
# 添加实例属性只针对于第一个创建的对象生效，要对所有类生效要使用类属性
# p2.Person("lisi",30)
# print(p2) 
# 添加类属性
# Person.addr = "beijing"
# print(p.addr)
# print(p2.addr)
