'''
Author: your name
Date: 2020-11-10 15:28:28
LastEditTime: 2020-11-11 14:13:19
LastEditors: Please set LastEditors
Description: yield用法
FilePath: \PythonStudent\Python_Test\Test12.py
'''
def fib(times):
    n = 0
    a,b = 0,1
    while  n<times:
        print("11111111111111111111111")
        yield b #yiled(放弃)函数执行到这个地方会交出cpu控制权，停止执行，调用next再继续
        a,b=b,a+b
        n=n+1
    return "done"

g = (fib(5))
# print(next(g))
# print(next(g))
print("G=%s",g)
for x in g:
    print(x)