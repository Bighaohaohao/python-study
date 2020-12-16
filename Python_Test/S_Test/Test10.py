'''
Author: your name
Date: 2020-11-10 14:32:52
LastEditTime: 2020-11-10 14:51:01
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Test10.py
'''
class Test(object):
    def __init__(self):
        self.__num=100
    
    def getNum(self):
        return self.__num
    
    def setNum(self,num):
        if num<100:
            self.__num=num
            
    num = property(getNum,setNum)
    
t = Test()
t.setNum(20)
# print(t.getNum())
print(t.num)