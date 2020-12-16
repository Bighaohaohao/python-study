class A(object):
    name = "张三"
    def test1(self):
        print("--------------A 的test1方法")

    # 类方法一定要在方法的上面加上修饰器 @classmethod，类方法的参数cls，代表当前的类
    @classmethod
    def test2(cls):
        cls.name = "李四"
        print("--------------A 的test1方法")

    # 静态方法，属于类。没有默认传递的参数，可以通过类的对象来进行调用，也可以通过类名进行调用
    @staticmethod
    def test3():
        print("---------------静态方法")

a = A()
a.test2()
A.test2()
print(A.name)
a.test3()
A.test3()
print(a.name)