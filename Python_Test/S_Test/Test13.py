'''
Author: your name
Date: 2020-11-10 17:15:49
LastEditTime: 2020-11-11 14:13:42
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Test13.py
'''
def fib(times):
    n = 0
    while  n<times:
        # print("11111111111111111111111")
        yield n*2
        n=n+1
    return "done"

g = (fib(5))
print("G=%s",g)
for x in g:
    print(x)