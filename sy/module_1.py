#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time;


class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

def getEmployeeToDisplay():
    test = Employee("sy",45789);
    test.displayEmployee();

    test.age = 25;
    print "age=",test.age;

def getTime() :
    print "module_1--getTime=", time.time();



# import socket               # 导入 socket 模块
#
# s = socket.socket()         # 创建 socket 对象
# host = socket.gethostname() # 获取本地主机名
# port = 12345                # 设置端口
# s.bind((host, port))        # 绑定端口
#
# s.listen(5)                 # 等待客户端连接
# while True:
#     c, addr = s.accept()     # 建立客户端连接。
#     print '连接地址：', addr
#     c.send('欢迎访问菜鸟教程！')
#     c.close()                # 关闭连接