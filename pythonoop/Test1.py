'''
Author: your name
Date: 2020-06-19 11:20:33
LastEditTime: 2020-12-16 13:48:28
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\pythonoop\Test1.py
'''
# 对象的属性
# class User:
#     def __str__(self):
#         return "用户名为%s,密码为%s"%(self.username,self.password)
    
#     def set_password(self,pw):
#         if len(pw) >= 6:
#             self.password=pw
#         else:
#             print("密码%s,长度错误"%pw)

# u1 = User()
# u1.username = "小米"
# u1.set_password("123456")
# print(u1)

# 动物类
# 先定义一个动物的类
class Animal:
    # 动物实例的初始化方法，需要提供动物类别和该类动物的叫声
    def __init__(self, kind, voice):
        self.kind = kind
        self.voice = voice
    # 让动物发出叫声的方法
    def speak(self):
        print(self.voice)

# 实例化四种动物对象
a = Animal("狗", "旺旺！")
b = Animal("猫", "喵！喵！")
c = Animal("牛", "哞！哞！")
e = Animal("二哈", "说人话！")

# 调用动物类的发声方法
a.speak()
b.speak()
c.speak()
e.speak()