# 访问列表中的值
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1[0]为 ", list1[0])
print ("list2[1:5]为 ", list2[1:5])

# 更新列表
list1 = ['Google', 'Runoob', 1997, 2000]
print ("列表list1 第二个元素为", list1[1])
list1[1] = '憨憨'
print ("更新后列表list1 第二个元素为", list1[1])

# 删除列表第三个元素、列表元素下标从0开始
del list1[2]
print ("删除list1列表第三个元素后",list1) 


# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"   #  不需要括号也可以
type(tup3)

# 创建空元组
tup1 = ()
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
tup4 = (10)
type(tup4)
tup5 = (10,)
type(tup5)

# 访问元组 元组可以使用下标索引来访问元组中的值，如下实例:
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
 
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

# 操作元组（增删改查）
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
tup3 = tup1 + tup2
print (tup3)

# 删除元组 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
tup = ('Google', 'Runoob', 1997, 2000)
 
print (tup)
# 以下操作删除元组会报错
# del tup
# print ("删除后的元组 tup : ")
# print (tup)

# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示
d = {"key1" : "value1", "key2" : "value2" }
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print ("dict['Alice']: ", dict['Alice'])

dict['Alice'] = 1234 # 更新信息
dict['school'] = '菜鸟' # 添加信息
print (dict)

# 删除字典元素
# 能删单一的元素也能清空字典，清空只需一项操作。
# 显示删除一个字典用del命令，如下实例：
# dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
# # 但这会引发一个异常，因为执行 del 操作后字典不再存在：
# del dict1['Name'] # 删除键 'Name'
# dict1.clear()     # 清空字典
# del dict1         # 删除字典
 
# print ("dict1['Age']: ", dict1['Age'])
# print ("dict1['School']: ", dict1['School'])



# 集合（set）是一个无序的不重复元素序列。

# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# 创建格式：
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print (basket)