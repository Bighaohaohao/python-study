# 属性私有化
class User:

    def __init__(self,pw):
        if len(pw) >= 6:
            self.__password = pw
        else:
            print("密码%s,长度错误"%pw)

    def __str__(self):
        self.__say_hello() # 私有属性可以从内部进行调用
        return "密码%s"%self.__password

    def __say_hello(self):
        print("私有属性你从外部调用不了嘿嘿嘿")

    def get_password(self):
        return self.__password
    
   
u1 = User("123456")
u1.__password = '1234567'  # 类里面的私有属性外部无法进行修改
# u1.__say_hello()
print(u1.get_password())
print(u1)
