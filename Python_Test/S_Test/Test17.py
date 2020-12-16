'''
Author: your name
Date: 2020-11-13 14:22:14
LastEditTime: 2020-11-13 15:15:12
LastEditors: Please set LastEditors
Description: 装饰器
FilePath: \PythonStudent\Python_Test\Test17.py
'''
# 装饰器其实就是一个闭包，把一个函数当做参数然后返回一个替代版函数
# 装饰器有2个特性：
# 1、可以吧被装饰的函数替换成其他函数
# 2、可以在加载模块时候立即执行
# 功能：1、引入日志 2、函数执行时间统计 3、执行函数前预备处理 4、执行函数后清理功能 5、权限校验等场景 6、缓存
def doca(func):
    def wrapper():
        print(func.__name__)
        func()
    return wrapper

def fun():
    print("-------------1----------------")
    
ret=doca(fun)
ret()

@doca
def fun2():
    print("-------------2----------------")
    
fun2()