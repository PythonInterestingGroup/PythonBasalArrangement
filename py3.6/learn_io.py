# -*- coding: utf-8 -*-
#author dm

try:
    f=open('123.txt','r')
    print(f.read())
finally:
    if f:
        f.close()
#等价于
with open('123.txt', 'r') as f:
    print(f.read())
f=open('123.txt','r')
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉

#读取二进制文件，比如图片、视频等等，用'rb'模式打开文件
f = open('test.jpg', 'rb')
print(f.read())

#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
f = open('123.txt', 'r', encoding='gbk')

#不规范的编码。非法编码字符，errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
f = open('123.txt', 'r', encoding='gbk', errors='ignore')

#写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
f = open('123.txt', 'w')
f.write('Hello, world!')
f.close()

with open('test.txt', 'w') as f:
    f.write('Hello, world!')


