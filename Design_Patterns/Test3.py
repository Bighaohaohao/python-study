class Person(object):

    def __init__(self,name):
        self.name = name

    def work(self,axt_type):
        print(self.name+"开始工作")
        # person完成work，需要使用一把斧头
        # 在原始社会需要一把石斧

        # axe = StoneAxe("花岗岩")
        # axe.cut_tree()

        # axe = SteelAxe("钢斧头")

        # 已经有工厂
        axe = Factory.create_axe("stone")
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

# 工厂类
class Factory(object):
    # 根据用户指定的类型生产斧头
    @staticmethod
    def create_axe(type):
        if type=="stone":
            return StoneAxe("花岗岩斧头")
        elif type=="steel":
            return SteelAxe("钢铁斧头")
        else:
            print("传入的类型不对")

p = Person("原始人")
p.work("stone")


