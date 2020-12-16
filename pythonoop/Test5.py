class  A:
    def test(self):
        print("A------test()")

class  B:
    def test(self):
        print("B------test()")

class C(B,A):
    def test1(self):
        print("C------test1()")

c = C()
# 多继承中两个父类拥有相同的方法，当自身没有该方法时，会按照继承顺序进行调用
print(C.__mro__)
c.test()