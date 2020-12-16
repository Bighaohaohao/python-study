# class User(object):
#     __instance = None
#     def __init__(self,name):
#         self.name = name

#     def __new__(cls,name):
#         if not cls.__instance: # 保证 object.__new__()方法只会执行一次
#             cls.__instance = object.__new__(cls)
#         return cls.__instance

# u1 = User("张三")
# u2 = User("李四")

# print (u1==u2) # == 为判断表达式，如果返回true,这两个对象是一个对象，并且内存地址相同
# print("u1对象的内存地址：%s,u2对象的内存地址：%s"%(id(u1),id(u2))) 
 
class User(object):
    __instance = None
    def __init__(self,name):
        self.name = name

    def __new__(cls,name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


u1 = User("zhangsan")
u2 = User("lisi")
print(u1.name)
print(u2.name)
print (u1==u2) # == 为判断表达式，如果返回true,这两个对象是一个对象，并且内存地址相同
print("u1对象的内存地址：%s,u2对象的内存地址：%s"%(id(u1),id(u2))) 