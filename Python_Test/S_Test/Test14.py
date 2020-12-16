'''
Author: your name
Date: 2020-11-11 14:25:12
LastEditTime: 2020-11-11 14:28:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Test14.py
'''
from collections import Iterable
a = isinstance([],Iterable)
print(a)
b = isinstance((),Iterable)
print(b)
c = isinstance("abc",Iterable)
print(c)
d = isinstance({},Iterable)
print(d)