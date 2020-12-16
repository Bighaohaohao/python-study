'''
Author: songpeihao
Date: 2020-11-05 14:53:54
LastEditTime: 2020-11-05 17:06:19
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Module_Test\Module1.py
'''
# 写一个工具方法，判断字符串是否为null，当字符串为None 为null，还有''还为null，还有'  '也为null
def isnull(str):
    if not str:
        return True
    elif str.strip()=='':
        return True
    else:
        return False
    
def test1():
    print("---------Module1中的test1------------")
    
#由python解释器主动执行该模块代码为了测试
if __name__ == '__main__': 
    # 模块在被导入的时候会自动被调用一次
    print(isnull(""))