'''
Author: your name
Date: 2020-11-17 15:13:05
LastEditTime: 2020-11-18 16:55:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Test20.py
'''

class Goods:
    __discount=0.5
    def __init__(self,name,price):
        self.name=name
        self.__price=price
    @property
    def price(self):
        return self.__price*self.__discount
    def set_price(self,new_price):
        if new_price and type(new_price) is int:  #这里保护了输入的数据为合法数据
            self.__price=new_price
        else:
            print('请输入正确的价格数据')

    @classmethod
    def set_discount(cls,new_discount): #将self替代为cls，用于这个类
        cls.__discount=new_discount
        return cls.__discount
apple=Goods('苹果',6)
Goods.set_discount(0.8)
print(apple.price)
