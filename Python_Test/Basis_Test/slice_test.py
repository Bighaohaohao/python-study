'''
Author: your name
Date: 2020-12-02 11:24:01
LastEditTime: 2020-12-03 09:44:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Basis_Test\slice_test.py
'''
list1 = [1,2,3,4,5,6]
list2 = [1,'a',[1,2,4],{4,5,6,'b'}]
# 查询元素的值
print (list1[0])
print(list2[3])
# 修改元素的值
list1 = [1,2,3,4,5,6]
list2 = [1,'a',[1,2,4],{4,5,6,'b'}]
list1[0] = "test"
print (list1[0])
list1 = [1,2,3,4,5,6]
list2 = [1,'a',[1,2,4],{4,5,6,'b'}]

# # 删除元素
# # 通过下标移除元素
# list1 = [1,2,3,4,5,6]
# list2 = [1,'a',[1,2,4],{4,5,6,'b'}]
# del list1[0]
# print (list1[0])
# list1 = [1,2,3,4,5,6]
# list2 = [1,'a',[1,2,4],{4,5,6,'b'}]

# # 通过值移除元素
# list2.remove(1)
# print(list2[0])

# # 通过下标删除元素
# list1 = [1,2,3,4,5,6]
# list2 = [1,'a',[1,2,4],{4,5,6,'b'}]
# list2.pop(0)
# print(list2[0])



# 切片
list1 = [1,2,3,4,5,6,7,8,9,10]
# 截取索引2、3、4、5的元素
a = list1[2:5]
# Python 打印嵌套list中每个数据（遍历列表）
for each_list in a:
    print(each_list)
print("--------------------------------------------------------------")
# 设置步长,第二份冒号后的值为步长
b = list1[3:9:4]
# 遍历列表的方法：遍历没一个元素本身
# for each_lists in b:
#     print(each_lists)
    
# 遍历列表的下标，通过下标取值
for i in range(len(b)):
    print(i,b[i])
    