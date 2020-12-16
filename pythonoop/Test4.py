# class Animal:
#     # 父类定义 __init__方法
#     def __init__(self):
#         print("-----------------动物的初始化---------")
#         self.color = "白色"

#     def eat(self):
#         print("--------------吃饭--------------------")

#     def sleep(self):
#         print("--------------睡觉--------------------")

# class Dog(Animal):
#     # 子类定义 __init__方法，且和父类的一样，是为方法的重写
#     def __init__(self,name):
#         super().__init__()  #主动调用父类的init方法
#         self.name = name

#     def eat(self):
#         super().eat()  #主动调用父类的init方法
#         print("狗自己的eat方法")

# dog = Dog("sengsi")  #如果子类对某个方法重写了，优先调用子类本身自己的方法
# print(dog.name)
# print(dog.color)
# dog.eat()

class Animal:
    # 父类定义 init 方法
    def __init__(self):
        print("---------------动物的初始化------------")
        self.color = "白色"

    def eat(self):
        print("---------------吃饭--------------------")
    
    def sleep(self):
        print("---------------睡觉--------------------")

class Dog(Animal):
    def __init__(self,name):
        super().__init__()
        self.name = name

dog = Dog("sengsi")
print(dog.name)
print(dog.color)
