'''
Author: your name
Date: 2020-11-23 14:55:03
LastEditTime: 2020-11-23 15:47:55
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Test24.py
'''
# @property装饰器
# Python内置的@property装饰器可以把类的方法伪装成属性调用的方式。也就是本来是Foo.func()的调用方法，变成Foo.func的方式。
class People:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        if isinstance(age,int):
            self.__age = age
        else:
            raise ValueError
        
    @age.deleter
    def age(self):
        print("删除年龄数据")

obj = People("jack",18)
print(obj.age)
obj.age = 19
print("obj.age:  ",obj.age)
del obj.age

# Python内置的builtins模块中的property()函数，为我们提供了第二种设置类属性的手段。
class People:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if isinstance(age,int):
            self.__age = age
        else:
            raise ValueError
        
    def del_age(self):
        print("删除年龄数据")
        
    # 通过语句age = property(get_age, set_age, del_age, "年龄")将一个方法伪装成为属性。其效果和装饰器的方法是一样的。

    # property()函数的参数：

    # 第一个参数是方法名，调用 实例.属性 时自动执行的方法
    # 第二个参数是方法名，调用 实例.属性 ＝ XXX时自动执行的方法
    # 第三个参数是方法名，调用 del 实例.属性 时自动执行的方法
    # 第四个参数是字符串，调用 实例.属性.__doc__时的描述信息。 
    age = property(get_age, set_age,del_age,"年龄")
    
obj = People("jack",18)
print(obj.age)
obj.age = 19
print("obj.age:  ",obj.age)
del obj.age