'''
Author: your name
Date: 2020-11-23 15:58:52
LastEditTime: 2020-11-23 16:34:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Test25.py
'''
import logging
import unittest
# 日志功能
# logging.basicConfig(level=logging.INFO)

# def func(s):
#     logging.info("s的数据类型为：s%" %type(s))
#     return s/10

# func(100)

# 单元测试之unittest

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('foo'.upper(),'Foo') # 断言执行'foo'.upper()后的结果是'FOO'
        
    def test_isupper(self):
        self.assertTrue('Foo'.isupper())
        self.assertFalse('Foo'.isupper())
        
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(),['hello','world'])
        # 当测试参数不是字符串的时候，应弹出类型异常
        with self.assertRaises(TypeError):
            s.split()
            
if __name__ == '__main__':
    unittest.main()
        
    