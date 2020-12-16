'''
Author: your name
Date: 2020-11-17 14:24:25
LastEditTime: 2020-11-17 14:48:50
LastEditors: Please set LastEditors
Description: python 类对象和实例对象动态添加方法
FilePath: \PythonStudent\Python_Test\Test19.py
'''
class Person():
    def __init__(self, name):
        self.name = name

def print_name(self):
    print(self.name)

p = Person('Li')
import types
p.print_name = types.MethodType(print_name, p)    # 绑定函数到对象
p.print_name()


@staticmethod
def print_abc():
    print('abc')

Person.print_abc = print_abc
Person.print_abc()

@classmethod
def print_123(cls):
    print('123')

Person.print_123 = print_123
Person.print_123()