def area(width,height):
    return width*height

w = 4
h = 5

print("width=", w,"height=", h,"area=", area(w,h))

def printme( str ):
    print(str)
    return

printme("我要调用用户自定义函数")
printme("再次调用")


# 参数传递
# 在 python 中，类型属于对象，变量是没有类型的：
# 以下代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。
a=[1,2,3]
a="Runoob"