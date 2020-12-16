'''
Author: your name
Date: 2020-11-09 14:54:25
LastEditTime: 2020-11-09 15:30:19
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Test8.py
'''
class Person():
    num=100
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def showInfo(self):
        print(self.name)
        print(self.age)
    
    # 类方法
    @classmethod
    def printNum(cls):
        print(cls.num)
    
    # 静态方法
    @staticmethod
    def add(a,b):
        return a+b
        
p = Person("特朗普",74)
p.showInfo()
p.printNum()
Person.printNum()
print(p.add(10,20))
print(Person.add(10,20))