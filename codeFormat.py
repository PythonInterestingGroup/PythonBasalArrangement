#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 编码格式
# 中文编码编码 -*- coding: UTF-8 -*- /coding=utf-8
print("现在是晚上九点钟，我在学习Python，哈哈哈！！！！！！！！！！！！！！1@@@@@@………………？？？？？？？？、、*****556")
ord('A')
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(chr(344))
print(ord('在'))
print(chr(22312))
print(ord('中'))
print(ord('文'))
# a = int('0x10', 9)
b = hex(16)
# print(a)
print(b)
print(str('\a\b'))

# 字符串转化为字节流用encode（）
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
byte = 'ABC'.encode('ascii')
print(byte)
# 纯英文的str可以用ASCII编码为bytes，内容是一样的，
# 含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错
a = '中文'.encode('utf-8')
print(a)

# 从磁盘读取字节流，转换为字符串用decode（）
str1 = b'abc'.decode('ascii')
print(str1)
str2 = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(str2)

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
len1 = len('abc')
print(len1)
len2 = len('中文')
print(len2)

len3 = len('abc'.encode('utf-8'))
print(len3)
len4 = len('中文'.encode('utf-8'))
print(len4)

# 格式化
# %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制整数
# name = input("请输入你的姓名：")
# print('hello\t' + name)

print('hell0,%s' % 'world')
print('hello,%s,your age is 0x%x' % ('lpp', 25))
print('growth rate is:%s%%' % 7)  # 字符串里面的%是一个普通字符时,需要转义，用%%来表示一个%

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位
name = input('你的名字是：')
lastY = float(input('去年你的成绩是：'))
thisY = float(input('你今年的成绩是：'))
rate = ((thisY - lastY) / lastY) * 100
if rate > 0:
    print('%s的成绩提升了%.1f个百分点,well done' % (name, rate))
elif rate == 0:
    print('%s的成绩和去年一样，要继续努力' % name)
else:
    print('%s的成绩下降了%.1f个百分点,要反思啊' % (name, rate))
