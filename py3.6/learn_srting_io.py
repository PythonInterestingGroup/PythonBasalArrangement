# -*- coding: utf-8 -*-
#author dm

#在内存中读写：stringIO

from io import StringIO

#把str写入StringIO,我们需要先创建一个StringIO，然后，像文件一样写入即可
f=StringIO()
print(f.write('hello')) #5
print(f.write('')) #0
print(f.write(' ')) #1
print(f.write('world!')) #6
print(f.getvalue())  #hello world!

#读取StringIO,可以用一个str初始化StringIO，然后，像读文件一样读取
f=StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s=f.readline()
    if s=='':
        break
    #print(s)
    print(s.strip())  #s.strip(rm) 删除s字符串中开头、结尾处，位于 rm删除序列的字符,当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')

#BytesIO 操作二进制数据
from io import BytesIO
f=BytesIO()
print(f.write('中文'.encode('utf-8')))  #6  #写入的不是str，而是经过UTF-8编码的bytes。
print(f.getvalue())  #b'\xe4\xb8\xad\xe6\x96\x87'

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
