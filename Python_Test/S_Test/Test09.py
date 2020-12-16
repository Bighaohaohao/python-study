'''
Author: your name
Date: 2020-11-09 15:38:25
LastEditTime: 2020-11-09 16:19:56
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Test9.py
'''
class Test(object):
    def __init(self):
        self.__num=100
      
# 类的私有属性无法在外部进行调用  
t = Test()
print(t.__num)