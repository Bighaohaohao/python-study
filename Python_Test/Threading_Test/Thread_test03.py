'''
Author: your name
Date: 2020-11-25 10:02:45
LastEditTime: 2020-11-27 09:54:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Threading_Test\Thread_test03.py
'''
# 线程锁
import threading
import time

number = 0

def plus():
    global number       # global声明此处的number是外面的全局变量number
    for _ in range(1000000):    # 进行一个大数级别的循环加一运算
        number += 1
    print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number))

# for i in range(2):      # 用2个子线程，就可以观察到脏数据
#     t = threading.Thread(target=plus)
#     t.start()
    
for i in range(2):     
    t = threading.Thread(target=plus)
    t.start()
    t.join()        # 添加这一行就让两个子线程变成了顺序执行  此处使用join方法，其实是让多线程变成了单线程，不推荐。


time.sleep(2)       # 等待2秒，确保2个子线程都已经结束运算。
print("主线程执行完毕后，number = ", number)
