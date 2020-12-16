'''
Author: your name
Date: 2020-11-24 14:26:29
LastEditTime: 2020-11-24 14:41:56
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Socket_Test\Client_test.py
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

ip_port = ('192.168.1.189', 9900)

s = socket.socket()     # 创建套接字

s.connect(ip_port)      # 连接服务器

while True:     # 通过一个死循环不断接收用户输入，并发送给服务器
    inp = input("请输入要发送的信息： ").strip()
    if not inp:     # 防止输入空信息，导致异常退出
        continue
    s.sendall(inp.encode())

    if inp == "exit":   # 如果输入的是‘exit’，表示断开连接
        print("结束通信！")
        break

    server_reply = s.recv(1024).decode()
    print(server_reply)

s.close()       # 关闭连接