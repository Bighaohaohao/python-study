# h = float(input("请输入身高"))
# w = float(input("请输入体重"))
# # print ("小明的身高为：%.2f,体重为%。2f"%(h,w))

# Bmi = w/(h**2)
# if Bmi < 18.5:
#     print("小明体重过轻")
# elif Bmi >= 18.5 and Bmi < 25:
#     print("小明体重正常")
# elif Bmi >= 25 and Bmi < 28:
#     print("小明体重过重")
# elif Bmi >= 28 and Bmi < 32:
#     print("小明体重肥胖")
# elif Bmi >= 28 and Bmi < 32:
#     print("小明体重严重肥胖")
# else:
#     print("不正常")

# 使用while循环打印一个矩形
# x = 1 #长
# y = 1 #宽

# while y<=10:
#     x = 1  
#     while x <= 10:
#         print ("*",end="")
#         x+=1
#     print("")
#     y+=1
# print("打印完成")


# 使用while循环打印一个九九乘法表
# x = 1 #一共打印九行
# while x <= 9:
#     y = 1 #代表列数
#     while y <= x:
#         print(y,"*",x,"=",x*y," ",end="")
#         y+=1
#     print("")
#     x+=1
# print("结束")

# continue用法
age =int(input("请输入年龄："))
i = 1
while True:
    if i == age :
        print("您的年龄为",i)
        break
    else:
        print("错了")
    i+=1