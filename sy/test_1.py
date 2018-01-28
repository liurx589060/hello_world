#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys;
import time;  # 引入time模块
import calendar;
import os;
import module_1;

from module_1 import getTime,getEmployeeToDisplay;
from module_2 import getCalendar;


# print "你好，世界！"
# print "hello world"
#
# if False:
#     print "this is true"
# else:
#     print "this is false"
#
# x = "the is custom x"
# print x
#
# list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# list2 = [ 'redf', 8944L ]
# print list[1:3]
# list[1] = 100005L
# print list + list2
#
#
# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
# print tinydict.keys()
# print tinydict.values()
#
# a = 2
# b = 20
# list = [1, 2, 3, 4, 5 ];
# if a in list:
#     print "a is in the list"
# else:
#     print "a is not in the list"
#
# count = 0
# while (count < 9):
#     print 'The count is:', count
#     count = count + 1
#
# print "Good bye!"
#
# count = 0
# while count < 5:
#    print count, " is  less than 5"
#    count = count + 1
# else:
#    print count, " is not less than 5"
#
# for letter in 'Python':  # 第一个实例
#     print '当前字母 :', letter
#
# fruits = ['banana', 'apple', 'mango']
# for fruit in fruits:  # 第二个实例
#     print '当前水果 :', fruit
#
# print "Good bye!"
#
# fruits = ['banana', 'apple', 'mango']
# for index in range(len(fruits)):
#     print '当前水果 :', fruits[index]
# print "Good bye!"
#
# print "My name is %s and weight is %d kg!" % ('Zara', 21)
#
# print time.time()
#
# localtime = time.localtime(time.time())
# print "本地时间为 :", localtime
#
# cal = calendar.month(2016, 2)
# print "以下输出2016年1月份的日历:"
# print cal;
#
# getTime()
# getCalendar(2018,1)
#
# fo = open("foo.txt","wb")
# fo.write("where is the place where the most beautiful is?")
# fo.closed
#
# fo = open("foo.txt", "r+")
# str = fo.read();
# print "读取的字符串是 : ", str
# # 关闭打开的文件
# fo.close()
#
# # 打开一个文件
# fo = open("foo.txt", "r+")
# str = fo.read(10);
# print "读取的字符串是 : ", str
#
# # 查找当前位置
# position = fo.tell();
# print "当前文件位置 : ", position
#
# # 把指针再次重新定位到文件开头
# position = fo.seek(0, 1);
# str = fo.read(10);
# print "重新读取字符串 : ", str
# # 关闭打开的文件
# fo.close()

# try:
#     fo = open("sy.txt", "a+")
#     fo.truncate()
#     while (1):
#         str = raw_input("请输入内容：")
#         if (str == "exit"):
#             fo.close()
#             break
#         else:
#             fo.write(str + "\n")
#             fo.flush()
# except IOError:
#     print "have exception"

# getEmployeeToDisplay()

# import json
# jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
#
# text = json.loads(jsonData)
# print text['a']

# from sys import stdout
#
# for j in range(2, 1001):
#     k = []
#     n = -1
#     s = j
#     for i in range(1, j):
#         if j % i == 0:
#             n += 1
#             s -= i
#             k.append(i)
#
#     if s == 0:
#         print j
#         for i in range(n):
#             stdout.write(str(k[i]))
#             stdout.write(' ')
#         print k[n]

from xml.etree import ElementTree as ET

liveFileName = 'live.xml'
syFileName = 'sy.xml'
baseFileName = 'base.xml'
baseStrings = ['pg_version_code','pg_version_name','pg_game_name','pg_package_name']
keepStrings = ['pg_facebook_login_id']
topTag = r'<?xml version="1.0" encoding="utf-8"?>' + '\n' + r'<resources>' + '\n'
endTag = r'</resources>'

def copyToDesFile(fileName,arrays):
    syFile = open(fileName,"w+")
    syFile.truncate()
    syFile.write(topTag)
    for str in arrays:
        syFile.write(str)
    syFile.write(endTag)
    syFile.close()

if os.path.exists(liveFileName):
    live_file = open(liveFileName, 'r')
    stringArrays = live_file.readlines()
    packageArrays = []
    keepArrays = []
    for str in stringArrays:
        if str.find(r'<string name') == -1 and str != '\n':
            stringArrays.remove(str)
        else:
            for param in baseStrings:
                if str.find(param) != -1:
                    packageArrays.append(str)

            for keepStr in keepStrings:
                if str.find(keepStr) != -1:
                    keepArrays.append(str)
            # print str
    # print stringArrays
    # 写入目标文件
    for str in packageArrays:
        stringArrays.remove(str)
    copyToDesFile(syFileName,stringArrays)
    # 写入基础文件中
    packageArrays += keepArrays
    print packageArrays
    copyToDesFile(baseFileName,packageArrays)
else:
    print "the live.txt is not found"
