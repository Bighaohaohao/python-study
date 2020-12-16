'''
Author: your name
Date: 2020-12-09 16:33:09
LastEditTime: 2020-12-10 14:56:39
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Interview_questions\question_02.py
'''
# 11、简述面向对象中__new__和__init__区别
# __init__是初始化方法，创建对象后，就立刻被默认调用了，可接收参数
class Bike:
    
    def __init__(self,newWheelNum, newColor):
        self.wheelNum = newWheelNum
        self.color = newColor
        
    def move(self):
        print('车会跑')
        
# 创建对象
BM = Bike(2, 'green')
print('车的颜色为：%s' %BM.color)
print('车轮数量为：%d' %BM.wheelNum)
BM.move()

# 1、__new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别
# 2、__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类（通过super(当前类名,
# cls)）__new__出来的实例，或者直接是object的__new__出来的实例
# 3、__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
# 4、如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面调用的__new__函数的第一个参数是cls来保证是当前类实例，
# 如果是其他类的类名，；那么实际创建返回的就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数
class A(object):
    def __init__(self):
        print("这是 init 方法",self)
        
    def __new__(cls):
        print("这是cls的ID",id(cls))
        print("这是new方法",object.__new__(cls))
        return object.__new__(cls)
    
A()
print("这是类A的id",id(A))

# 12、简述with方法打开处理文件帮我我们做了什么？
