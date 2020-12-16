class User(object):
    name = "张三"  # 共有属性
    __password = '123456' # 私有属性

    def __init__(self,sex,username):
        self.sex = sex
        self.username = username

class Wx_User(User):
    pass

u = User("男","goldbin")
print(u.name)
print(Wx_User.name) # name丛父类继承过来的，name属于类属性，可以直接通过类进行访问，也可以通过类的对象进行访问
# print(u.__password)  #私有属性无法从类外部进行访问

# 类属性修改 只能通过类来修改
User.name = "李四"
u.name = "李四" # 本质上没有修改类属性，只是给该对象定义了一个对象属性 name,且赋值为 王五
print(u.name)
# print(User.name)
del u.name # 本质上删除了对象的name属性，并没有删除类的属性
print(User.name)