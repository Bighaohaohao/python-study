"""
Author: your name
Date: 2020-11-25 09:52:52
LastEditTime: 2020-11-25 09:58:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
"""


# 自定义线程类
# 对于threading模块中的Thread类，本质上是执行了它的run方法。因此可以自定义线程类，让它继承Thread类，然后重写run方法。
import threading


class MyThreading(threading.Thread):
    def __init__(self, func, arg):
        super(MyThreading, self).__init__()
        self.func = func
        self.arg = arg
        
    def run(self):
        self.func(self.arg)


def my_func(args):
    """[summary]
    你可以吧任何你想让线程做的事定义在这里
    Args:
        args ([type]): [description]
    """
    pass


obj = MyThreading(my_func,123)
obj.start()
