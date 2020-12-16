class Person(object):
    def __init__(self,name):
        self.name = name

    def work(self):
        print(self.name+"开始工作")
        factory = Steel_Axe_Factory()
        axe =factory.create_axe()
        axe.cut_tree()

class Axe(object):
    def __init__(self,name):
        self.name = name

    def cut_tree(self):
        print("%s斧头开始砍树"%self.name)

class StoneAxe(Axe):
    def cut_tree(self):
        print("使用石头做的斧头砍树")

class SteelAxe(Axe):
    def cut_tree(self):
        print("使用钢铁做的斧头砍树")

# 工厂方法模式 替代之前的全局函数(Test5.py)
# 根据用户指定的类型生产斧头
# 抽象工厂角色
class Factory(object):
    pass

# 具体工厂角色
class Stone_Axe_Factory(Factory):
    def create_axe(self):
        return StoneAxe("花岗岩斧头")

# 具体工厂角色
class Steel_Axe_Factory(Factory):
    def create_axe(self):
        return SteelAxe("花岗岩斧头")

p = Person("原始人")
p.work()


