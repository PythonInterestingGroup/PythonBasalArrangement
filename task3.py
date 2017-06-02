#!/usr/bin/env python
# -*- coding: utf-8 -*-
#字符串和编码
print ord('a')
print chr(120)
print u'中文'
print u'中'
print u'\u4e2d'
print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'
print 'abc'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print u'\u4e2d\u6587'
print len(u'ABC')
print len('ABC')
print len(u'中文')
print len('中文')
print 'hello,%s' % 'world'
print 'Hi,%s,you have $%d.' % ('DJX',10000000000)
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print '%2d-%02d' % (3,1) #结果：3-01
print '%.2f' % 3.1415926 #结果：3.14
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print 'Age: %s. Gender： %s' % (25,True)  #结果：Age:25. Gender：True
# ，用%%来表示一个%
print 'qrowth rate: %d%%' % 20 #结果：qrowth rate: 20%

#list
list1 =['张三','李四','王二']
list2 =['AAA','BBB','CCC','DDD']
print list1,list2 #结果：['\xe5\xbc\xa0\xe4\xb8\x89', '\xe6\x9d\x8e\xe5\x9b\x9b', '\xe7\x8e\x8b\xe4\xba\x8c'] ['AAA', 'BBB', 'CCC', 'DDD']
print len(list1),len(list2) #结果：3 4
print list2[0] #结果：AAA
#索引去-1获取list最后一个元素，-2倒数第二个元素，以此类推，注意不能越界
print list2[-1] #结果：DDD
#往list中追加元素到末尾
list2.append('EEEE')
print list2 #结果：['AAA', 'BBB', 'CCC', 'DDD', 'EEEE']
#把元素插入到指定的位置，比如索引号为1的位置
list2.insert(1,'FFFF')
print list2 #结果：['AAA','FFFF', 'BBB', 'CCC', 'DDD', 'EEEE']
#删除list末尾的元素，用pop()方法
list2.pop()
print list2  #结果：['AAA','FFFF', 'BBB', 'CCC', 'DDD']
#删除指定位置的元素，用pop(i)方法，其中i是索引位置：
list2.pop(1)
print list2  #结果：['AAA', 'BBB', 'CCC', 'DDD']
# 把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
list2[1]='FFFFF'
print list2 #结果：['AAA', 'FFFFF', 'CCC', 'DDD']
# list里面的元素的数据类型也可以不同，比如：
list3 = ['aaaa',23,True]
print list3 #结果：['aaaa',23,True]
# list元素也可以是另一个list
list4 = ['aaa','bb',['123','234'],'cc']
print list4 #结果：['aaa','bb',['123','234'],'cc']

p = ['asp','php']
s = ['ios','htm5',p,'java']
print  s       #结果：['ios','htm5',['asp','php'],'java']
print  p[1]    #结果：php
print  s[2][1] #结果：php
# 要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。

# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
L = []
print len(L) #结果：0

# tuple
# tuple和list非常类似，但是tuple一旦初始化就不能修改

myTuple = ('JJ','VN','RV',"JS")
#没有append()，insert()这样的方法
print myTuple #结果：('JJ','VN','RV',"JS")

#定义一个空的tuple
t = ()
print t #结果：()

# 只有1个元素的tuple定义时必须加一个逗号','
t1 = (1)
t2 = (1,)
print t1 #结果：1
print t2 #结果：(1,)

# “可变的”tuple:
t3 = ('a','b',['A','B'])
t3[2][0] = 'X'
t3[2][1] = 'Y'
print t3 #结果:('a', 'b', ['X', 'Y'])
#t3[2]本身是个可变的list ，t3[2]里面的元素可以变，但是t3[0]、t3[1]不可变,tuple的指向是不可变的



# 条件判断和循环
# 条件判断
#如果if语句判断是True，就把缩进的两行print语句执行了
age = 20
if age>=18:
    print 'your age is',age
    print  'YES'
elif age>=15:
    print 'your age is',age
else:
    print 'NO'
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = 10
if x:
    print 'True'
else:
    print 'False'

#循环
#for-in循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

sum = 0
for x in  [0,1,2,3,4,5,6,7,8,9,10]:
    sum+=x
print 'sum =',sum #结果：sum = 55

sum = 0
sum1 = 0
for x in  range(10):
    sum += x
for x in range(11):
    sum1 += x
print 'sum =',sum
print 'sum1 =',sum1
#rang(10)表示0-9的整数序列，rang(11)表示0-10的整数序列

#while循环
# while循环，只要条件满足，就不断循环，条件不满足时退出循环,循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出
sum = 0
n = 10
while n > 0:
    sum += n
    n -= 1
    print 'n =',n
print 'sum =',sum

#从raw_input()读出的值是字符串
birth = raw_input('请输入birth :')
print birth

if birth>90:
    print '判断结果为：YES'
else:
    print '判断结果为：NO'
#以上不管输入的是100，还是80，最终打印出来都是YES

if int(birth)>90:
    print '判断结果为：YES'
else:
    print '判断结果为: NO'
#可以使用int()把字符串转出整型

# 使用dict和set
# dict
myDict = {'jianghao':'60kg','yueyue':'80kg','daizi':'70kg','sufei':'85kg'}
print 'myDict =',myDict
print 'jianghao的体重:',myDict['jianghao']

myDict['yueyue'] = '75kg'
print 'yueyue的体重',myDict['yueyue']
print 'tanjiankang' in myDict #结果:False 使用in判断key是否存在
print  myDict.get('tanjiankang') #结果:None key不存在时返回none
print  myDict.get('yueyue')  #结果:75kg
print  myDict.get('tanjiankang',-1) #结果:-1 key不存在时返回指定的value -1
print  myDict.get('sufei',-1)  #结果:85kg
#用pop(key)方法，对应的value也会从dict中删除
myDict.pop('sufei')
print  'myDict =',myDict
