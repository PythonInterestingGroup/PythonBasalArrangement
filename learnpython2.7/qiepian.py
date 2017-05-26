# _*_ coding: utf-8 _*_
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L

print L[0],L[1],L[2]

r=[]
n=3
for i in range(n):
    r.append(L[i])
print r

print L[0:3]
print L[:3]
print L[1:3]
print L[-2:]
print L[-2:-1]

L=range(20)
print L

print L[:10]
print L[-10:]
print L[10:20]

#前10个数，每两个取一个
print L[:10:2]

#所有数，每5个取一个
print L[::5]

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print (0,1,2,3,4,5)[:3]

#字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print 'abcdefg'[:3]
print 'abcdefm'[::2]
