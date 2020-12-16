'''
Author: your name
Date: 2020-11-20 15:36:39
LastEditTime: 2020-11-20 15:57:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Test22.py
'''
# 类装饰器 
class Test():
    # 使用__call__()方法可以使得其能在外部通过类的实例进行调用
    def __call__(self):
        print("call me!")
        
t=Test()
t()