'''
Author: your name
Date: 2020-11-26 11:03:39
LastEditTime: 2020-11-26 11:14:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Threading_Test\Thread_test05.py
'''
import time
import queue
import threading

q = queue.Queue(10) # 生成一个队列，用来保存包子，最大数量为 10
def productor(i):
    # 厨师不停的每2S做一个包子
    while True:
        q.put("厨师 %s 做的包子! " % i)
        time.sleep(2)
        
def consumer(j):
    # 厨师不停的每2S做一个包子
    while True:
        print("顾客 %s 吃了一个 %s"%(j,q.get()))
        time.sleep(1)
        
# 实例化三个厨师（生产者）
for i in range(3):
    t = threading.Thread(target=productor,args=(i,))
    t.start()
    
# 实例化10个厨师（生产者）
for j in range(10):
    v = threading.Thread(target=consumer,args=(j,))
    v.start()     