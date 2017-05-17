# string and coding

# Unicode(http://www.jianshu.com/p/dbc65e439311)
# 255 / 65,535 / 4,294,967,295

print(ord('A')) # ord()
print(chr(66)) # chr()
print(chr(25991))
print('\u4e2d\u6587') # unicode scalar

x = b'ABC' # bytes 类型 => 每个字符只占一个字节 ??

'ABC'.encode('ascii') # => encode
z = '中文'.encode('utf-8')
print(z)
b'ABC'.decode('ascii') # => decode
dz = z.decode('utf-8')
print(dz)

print("z length = ", len(z)) # 字符数
print("dz lenght = ",len(dz)) # 字节数

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#　string format

name = input("enter your name:")
print("hello %s" % name)
print("I have %d ge %f ge %x" % (11, 1.22, 0x111))

print("%.2f - %2d -- %02d" % (3.1415, 3, 3))

print("%d%%" % 7)

