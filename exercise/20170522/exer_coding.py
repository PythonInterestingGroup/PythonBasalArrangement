#!/usr/bin/env/ python3
# -*-  coding: utf-8 -*- 

a = "H"
b = "好"

c = "hello world"
d = "你好 世界"

e = b'hello world'

print("ord(%s):"%(a),ord(a))
print("ord(%s):"%(b),ord(b))  

print("chr(72):",chr(72))
print("chr(22909):",chr(22909))

print(r'\u4e2d\u6587 -->','\u4e2d\u6587')

print("c type -->",type(c))
print("e type -->",type(e))

## encode  str --> bytes
print("c --E-ascii-->" , c.encode('ascii'))
print("c --E-utf-8-->" , c.encode('utf-8'))
print("d --E-utf-8-->" , d.encode('utf-8'))

## decode  bytes --> str
print("b\'hello world\' --D-ascii-->" , b'hello world'.decode('ascii'))
print("b\'hello world\' --D-utf-8-->" , b'hello world'.decode('utf-8'))

print("b\"你好 世界\" --D-utf-8-->" , b'\xe4\xbd\xa0\xe5\xa5\xbd \xe4\xb8\x96\xe7\x95\x8c'.decode('utf-8'))

print("\'你好 世界\' length:",len(d))
print("bytes:b\'"+r"\xe4\xbd\xa0\xe5\xa5\xbd \xe4\xb8\x96\xe7\x95\x8c"+"\' length:"
,len(d.encode('utf-8'))
,"str:"+b'\xe4\xbd\xa0\xe5\xa5\xbd \xe4\xb8\x96\xe7\x95\x8c'.decode('utf-8'))


print("utf-8 =>",len("编号89757A".encode('utf-8')))
print("gbk =>",len("编号89757A".encode('gbk')))
print("unicode =>",len("编号89757A"))