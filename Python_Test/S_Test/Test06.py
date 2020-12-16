while True:
    try:
        x = int(input("请输入一个数字"))
    except ValueError:
        print("您输入的不是数字啊")