'''
Author: your name
Date: 2020-11-25 10:53:06
LastEditTime: 2020-11-25 10:59:38
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Process_Test\Process_Test.py
'''
from multiprocessing import Process
import os

def run_proc(name):
    print('运行子进程%s(%s)......'%(name,os.getpid()))

if __name__ == '__main__':
    print('父进程%s'%os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('子进程将开始')
    p.start()
    p.join()
    print('子进程结束')