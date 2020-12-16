import sys

# list = [1,2,3,4]
# it = iter(list) # 创建迭代器对象
# while True:
#     try:
#          print (next(it))
#     except StopIteration:
#         sys.exit()

class Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
       

myclass = Numbers()
myiter = iter(myclass)

for x in myiter:
    print(x)