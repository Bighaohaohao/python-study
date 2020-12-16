'''
Author: your name
Date: 2020-11-11 14:41:51
LastEditTime: 2020-11-11 15:18:13
LastEditors: Please set LastEditors
Description: 闭包：内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包
FilePath: \PythonStudent\Python_Test\Tets15.py
'''
def test(number):
    # 在函数内部再定义一个函数，并且这个函数用到了外边函数的变量
    def test_in(number_in):
        print("in test_in函数,number_in is%d" %number_in)
        return number+number_in
    # 其实此处返回的就是闭包的结果
    return test_in