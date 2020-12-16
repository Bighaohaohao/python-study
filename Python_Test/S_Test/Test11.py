'''
Author: your name
Date: 2020-11-10 14:32:52
LastEditTime: 2020-11-10 15:18:10
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Test10.py
'''
class Test(object):
    def __init__(self):
        self.__num=100
    
    @property
    def num(self):
        return self.__num
    
    @num.setter
    def num(self,num):
        if num<100:
            self.__num=num
    
t = Test()
t.num =10
print(t.num)