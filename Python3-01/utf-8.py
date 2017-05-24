#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

s = r''' 纯因为的 str 可以用 ASCII 编码为 bytes/ 字节
 含有中文的str可以用 utf-8编码为 bytes ''' 	

print(s)
print('中文的 utf-8 编码为:','中文'.encode('utf-8'))
print('中文的字符长度为:', len('中文'))
print('中文的字节长度为:', len('中文'.encode('utf-8')))

s1 = 72
s2 = 85
r = s2/ s1
print('小明今年的成绩85交去年的72提升了%.1f倍'%r)