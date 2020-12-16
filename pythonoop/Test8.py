class User(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print("对象已经构建完成，由解释器自动回调的方法，对象初始化")

    # new方法是当对象构建的时候由解释器自动回调的方法，该方法必须返回当前类的对象。
    def __new__(cls,username,password):
        print("User类的对象开始构建")
        return object.__new__(cls)

    def __str__(self):
        return "用户名为%s,密码%s"%(self.username,self.password)
        
u = User("张三","123456")
print(u)