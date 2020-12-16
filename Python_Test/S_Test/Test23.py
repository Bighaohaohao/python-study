'''
Author: your name
Date: 2020-11-23 11:51:33
LastEditTime: 2020-11-23 14:33:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Test23.py
'''
# 成员未得到保护和访问限制
# class People:
#     title = "人类"
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def print_age(self):
#         print('%s: %s' %  (self.name, self.age))
        
# obj = People("jack",12)
# obj.age = 18
# obj.print_age()
# print(People.title)

# 在Python中，如果要让内部成员不被外部访问，可以在成员的名字前加上两个下划线__，这个成员就变成了一个私有成员（private）。私有成员只能在类的内部访问，外部无法访问。
# class People:
#     title ="人类"
    
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
        
#     def print_age(self):
#         print("$s: %s" %(self.__name, self.__age))
        
# obj = People("jack",12)
# obj.__name

# 那外部如果要对__name和 __age进行访问和修改呢？在类的内部创建外部可以访问的get和set方法！
    
class People:
    title ="人类"
    
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        
    def print_age(self):
        print("$s: %s" %(self.__name, self.__age))
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self,name):
        self.__name = name
        
    def set_age(self,age):
        # 作用：保护数据、提供外部访问接口、还可以添加对数据的检测、处理、加工等操作。
        # 在设置年龄之前对参数进行检测，如果参数不是传入int类型，则报错
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError
        
obj = People("jack",12)
obj.get_name()
obj.set_name("tom")
print(People.title)

    
