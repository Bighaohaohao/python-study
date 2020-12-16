# class User(object):
#     __instance = None
#     def __init__(self,name):
#         self.name = name

#     @classmethod
#     def get_instance(cls,name):
#         if not cls.__instance: # 如果__instance = None则满足该条件
#             cls.__instance = User(name)
#         return cls.__instance

# # u1 = User("张三")
# # u2 = User("李四")
# u1 = User.get_instance("张三")
# u2 = User.get_instance("李四")
# print (u1==u2) # == 为判断表达式，如果返回true,这两个对象是一个对象，并且内存地址相同
# print("u1对象的内存地址：%s,u2对象的内存地址：%s"%(id(u1),id(u2))) 
# print(u1.name)
# print(u2.name)

class User(object):
    __instance = None
    def __init__(self,name):
        self.name = name

    @classmethod
    def get_instance(cls,name):
        if not cls.__instance:
            cls.__instance = User(name)
        return cls.__instance

u1 = User.get_instance("张三")
u2 = User.get_instance("李四")
print(u1==u2)
print(id(u1),id(u2))

print(u1.name)
print(u2.name)