# 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 方法：类中定义的函数。
# 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
# 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
# 局部变量：定义在方法中的变量，只作用于当前实例的类。
# 实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
# 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
# 实例化：创建一个类的实例，类的具体对象。
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

# 以下创建了一个新的类实例并将该对象赋给局部变量 x，x 为空的对象
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world!'

# 实例化类
X = MyClass()
# 访问类的属性和方法
print("MyClass类的属性i为",X.i)
print("MyClass类的方法f输出为",X.f())


class ComPlex():
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

Y = ComPlex(5,10)
print(Y.r, Y.i)

# 类的方法
# 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。

# 类定义
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# # 实例化类
# p = people('runoob',10,30)
# p.speak()

class people:
    name = ''
    age = 0
    weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

p = people('runoob',10,30)
p.speak()