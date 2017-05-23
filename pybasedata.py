#!/usr/bin/env python
# -*- coding: utf-8 -*-


#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print 'I\'m \"OK\"!'

print 'I\'m learning\nPython.'

print '\\\n\\'

print '\\\t\\'

#Python还允许用r''表示''内部的字符串默认不转义
print r'\\\t\\'

#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print '''line1
line2
line3'''

print r'''line1
...line2
...line3'''

print r'''line1
line2
line3'''

print 3>2
print 3>5

print True and True
print True and False

print True or True

print not True

age=1
if age>=18:
    print 'adult'
else:
    print 'teenager'

a=123
a='abc'


#普通的字符串'ABC'在Python内部都是ASCII编码的
#Python提供了ord()和chr()函数，可以把字母和对应的数字相互转换
print ord('A')
print chr(65)

#以Unicode表示的字符串用u'...'表示
print u'中文'

print u'中'
print u'\u4e2d'

#字符串'xxx'虽然是ASCII编码，但也可以看成是UTF-8编码，而u'xxx'则只能是Unicode编码
#把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法
print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')

print len(u'ABC')
print len('ABC')
print len(u'中文')
print len('\xe4\xb8\xad\xe6\x96\x87')

#把UTF-8编码表示的字符串'xxx'转换为Unicode字符串u'xxx'用decode('utf-8')方法
print 'abc'.decode('utf-8')
print  '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

#在Python中，采用的格式化方式和C语言是一致的，用%实现
print  'Hello, %s' % 'world'
print  'Hi, %s, you have $%d.' % ('Michael', 1000000)

#在字符串内部，%s表示用字符串替换，%d表示用整数替换
#常见的占位符有：
#%d	整数
#%f	浮点数
#%s	字符串
#%x	十六进制整数

print '%2d-%02d' % (3, 1) #格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print  '%.2f' % 3.1415926 #保留两位小数

print  'Age: %s. Gender: %s' % (25, True)

print u'Hi, %s' % u'Michael'
print  'growth rate: %d %%' % 7 #%%来表示一个%


#List
#list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print len(classmates)
print classmates[0]
print classmates[1]
print classmates[2]
print classmates[-1]
print classmates[-2]
print classmates[-3]

classmates.append('Adam')
print classmates

classmates.insert(1, 'Jack') #将元素插入表指定位置，索引为1的位置
print classmates

classmates.pop() #删除末尾的元素
print classmates

classmates.pop(1)#删除索引位置为1的元素
print classmates

classmates[1]='Sarah'#替换索引位置为1的元素，直接赋值
print classmates

L=['Apple', 123, True] #list元素类型可不同

s = ['python', 'java', ['asp', 'php'], 'scheme'] #list元素也可以是另一个list
print len(s)
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']

L=[]
print len(L)


#tuple
#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
#classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
classmates = ('Michael', 'Bob', 'Tracy')

t=(1,2)
print t

#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
x=(1,)

y = ('a', 'b', ['A', 'B'])
y[2][0] = 'X'
y[2][1] = 'Y'
print y
#tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

#if
#if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age=20
if age>=6:
    print 'teenager'
elif age>=18:
    print 'adult'
else:
    print 'kid'

#for..in
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

#计算1-10的整数之和
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print sum

sum=0
for x in range(101):
    sum=sum+x
print sum

#while循环，只要条件满足，就不断循环，条件不满足时退出循环。
#计算100以内所有奇数之和，可以用while循环实现
#在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print sum

#dict
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']

d['Adam'] = 67

#判断key是都存在,
#1通过in判断key是否存在
#2通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value,注意：返回None的时候Python的交互式命令行不显示结果。
print 'Thomas' in d 
d.get('Thomas')
d.get('Thomas', -1)

d.pop('Bob') #要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print d

#set
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 3])
print s

#注意，传入的参数[1, 2, 3]是一个list，而显示的set([1, 2, 3])只是告诉你这个set内部有1，2，3这3个元素，显示的[]不表示这是一个list。

#重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print s

#add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print s

#remove(key)方法可以删除元素
s.remove(4)
print s

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
