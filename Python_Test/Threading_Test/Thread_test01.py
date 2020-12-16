'''
Author: your name
Date: 2020-11-24 10:29:25
LastEditTime: 2020-11-25 09:48:49
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Test26.py
'''
import threading
import time
# 有两种方式来创建线程：一种是继承Thread类，并重写它的run()方法；
# class MyThread(threading.Thread):
#     def __init__(self, thread_name):
#         # 注意：一定要显式的调用弗雷德初始化函数 super() 函数是用于调用父类(超类)的一个方法。
#         super(MyThread, self).__init__(name=thread_name)
        
#     # 线程被cpu调度后自动执行的方法
#     def run(self):
#         print("%s正在运行中......" % self.name)
        
# if __name__ == '__main__':    
#     for i in range(10):
#         MyThread("thread-" + str(i)).start()


# 另一种是在实例化threading.Thread对象的时候，将线程要执行的任务函数作为参数传入线程
# arg代表接收的数据是一个字典
# def show(arg):
#     time.sleep(1)
#     print('thread' +str(arg)+" running....")

# if __name__ == '__main__':
#     for i in range(10):
#         t = threading.Thread(target=show, args=(i,))
#         # 启动线程，等待CPU调度
#         t.start()
        
# 在多线程执行过程中，有一个特点要注意，那就是每个线程各执行各的任务，不等待其它的线程，自顾自的完成自己的任务，比如下面的例子：
# def dowaiting():
#     print('star waiting:', time.strftime('%H:%M:%S'))
#     time.sleep(3)
#     print('stop waiting', time.strftime('%H:%M:%S'))

# t = threading.Thread(target=dowaiting())
# t.start()
# # 确保线程t已经启动
# time.sleep(1)
# print('start job')
# print('end job')

# 有时候我们希望主线程等等子线程，不要“埋头往前跑”。那要怎么办？使用join()方法！如下所示：
# def dowaiting():
#     print('star waiting:', time.strftime('%H:%M:%S'))
#     time.sleep(3)
#     print('stop waiting', time.strftime('%H:%M:%S'))

# t = threading.Thread(target=dowaiting())
# t.start()
# # 确保线程t已经启动
# time.sleep(1)
# print('start join')
# # 将一直堵塞
# t.join()
# print('end join')

# 可以使用setDaemon(True)把所有的子线程都变成主线程的守护线程，当主线程结束后，守护子线程也会随之结束，整个程序也跟着退出。
def run():
    print(threading.current_thread().getName(),"开始工作")
    time.sleep(2)  # 子线程停2s
    print("子线程工作完毕")
    
for i in range(3):
    t = threading.Thread(target=run,)
    t.setDaemon(True)  # 把子线程设置为守护线程，必须在start()之前设置
    t.start()
    
time.sleep(1) # 主线程停1S
print("主线程结束了!!！")
print(threading.active_count()) #输出活跃的线程数