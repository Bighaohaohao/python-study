# # 定义一个类
# class Car:
#     def start(self):
#         print("汽车启动")

#     def print_car_inf(self):
#         print("车的名字是：%s,颜色为：%s"%(self.name,self.color))

# # 构建一个对象
# c = Car()
# c.name = "宝马"
# c.color = "蓝色"
# c.print_car_inf()
# c.start()

class People:
    def eat(self):
        print("人吃饭")

    def print_people(self):
        print("人的名字是: %s,年龄为: %s"%(self.name,self.age))

# 实例化对象
p = People()
p.name = "小明"
p.age = 18
p.print_people()
p.eat()