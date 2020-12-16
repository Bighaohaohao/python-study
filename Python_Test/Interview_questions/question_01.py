'''
Author: your name
Date: 2020-12-08 11:04:35
LastEditTime: 2020-12-11 10:25:42
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Interview_questions\question_01.py
'''
# 1、一行代码实现1--100之和？
a=sum(range(1,101))
print(a)

# 2、如何在一个函数内部修改全局变量？
a = 10
def test(self):
    global a  # 使用global修改全局变量
    a = 100

print(a)

# 3、列出4个python标准库？
# os：提供了不少与操作系统相关联的函数
# sys：通常用于命令行参数
# re：正则匹配
# math：数学运算

# 4、字典如何删除键和合并两个字典
# del和update方法
dic = {"name":"ZS","age":18}
del dic["name"]   # 删除键

dic2 = {"name":"LS"}
dic.update(dic2)

# 1  直接遍历字典获取键，根据键取值
for key in dic:
    print(key, dic[key])


dic = {"name":"ZS","age":"18"}
for key in dic:
    print(key,dic[key])
    
dic2 = {"name":"LS","sex":"男"}
dic.update(dic2)
for key in dic:
    print(key,dic[key])
    
# 6、实现列表去重
list = [11,12,12,13,13,14,15]  # 定义一个列表 list
a = set(list)  # 通过集合去重
# 转为列表
for list in a:
    print(list)
    
# 7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
# *args是用来发送一个非键值对的可变数量参数列表给一个函数
def demo(args_f,*args_v):
    print(args_f) 
    for x in args_v:
        print(x)
        
        
demo('a','b','c','d')

# **kwargs是用来将不定长度的键值对，作为参数传递给一个函数
def demo1(**args_v):
    for k,v in args_v.items():
        print(k,v)
    
demo1(name = "kobe")

# 8、python2和python3的 range(100) 的区别
# python2返回列表；python3返回迭代器


# 9、一句话解释什么样的语言能够用装饰器?
# 函数可以作为参数传递的语言，可以使用装饰器

# 10、python内建数据类型有哪些

# 整型--int

# 布尔型--bool

# 字符串--str

# 列表--list

# 元组--tuple

# 字典--dict


