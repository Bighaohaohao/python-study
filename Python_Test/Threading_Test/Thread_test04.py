'''
Author: your name
Date: 2020-11-25 11:05:41
LastEditTime: 2020-11-25 11:14:34
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Threading_Test\Thread_test04.py
'''
# 互斥锁
# 互斥锁是一种独占锁，同一时刻只有一个线程可以访问共享的数据。
# 使用方法:初始化锁对象，然后将锁当做参数传递给任务函数，在任务中加锁，使用后释放锁。
import threading
import time

number = 0
lock = threading.Lock()

def plus(lk):
    global number   # global声明此处的number是外面的全局变量numbe
    lk.acquire()    # 开始加锁
    for _ in range(1000000):  # 进行一个大数级别的循环加一次运算
        number +=1
    print("子线程%s运算结束后，number =%s" % (threading.current_thread().getName(),number))
    lk.release()    # 释放所，让别的线程也可以访问number
    
if __name__ =='__main__':
    for i in range(2):
        t = threading.Thread(target=plus,args=(lock,))
        t.start()
    time.sleep(2)
    print("主线程执行完毕后，number = ",number)
    