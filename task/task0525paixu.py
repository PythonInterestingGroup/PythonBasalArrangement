#!/usr/bin/env python
# -*- coding: utf-8 -*-


#对第二列进行从小到大排序，在对第三列从大到小排序
students =[('john','B',15),('jane','A',12),('dave','B',10),('ethan','C',20),('peter','B',20),('mike','C',16)]
print students

#for student in students:
    #print student
    
for i in range(len(students))[::-1]:
    #print students
    #print students[i][1]
    for j in range(i):
        if students[j][1]>students[j+1][1]:
            students[j],students[j+1]=students[j+1],students[j]
        if students[j][1]==students[j+1][1]:
            if students[j][2]<students[j+1][2]:
                students[j],students[j+1]=students[j+1],students[j]

for student in students:
    print student

print students


students =[('john','B',15),('jane','A',12),('dave','B',10),('ethan','C',20),('peter','B',20),('mike','C',16)]
for i in range(0,len(students)):
    for j in range(i+1,len(students)):
        if students[i][1]>students[j][1]:
            students[i],students[j]=students[j],students[i]
        if students[i][1]==students[j][1]:
            if students[i][2]<students[j][2]:
                students[j],students[i]=students[i],students[j]

for student in students:
    print student

#用sorted函数
#reverse = True 表示倒序删除
students =[('john','B',15),('jane','A',12),('dave','B',10),('ethan','C',20),('peter','B',20),('mike','C',16)]
def by_degree(t):
    return student[1]
def by_score(t):
    return students[2]
def by_cj(t):
    return student[1],student[2]

#2.7有错误，待更新
print 's:',sorted(students,itemgetter(1))
print students
print 's1:',sorted(students,by_degree,reverse=True)

print 's2:',sorted(students,by_score,reverse=True)

print 's3:',sorted(students,by_cj,reverse=False)

#3.4用法
#print(sorted(students, key=itemgetter(0)))
#print(sorted(students, key=lambda t: t[1]))
#print(sorted(students, key=itemgetter(1), reverse=True))

#［::-1] 是个list的切片方法，步移为-1，从list的开始到最后
#冒泡排序
array = [1,2,3,6,5,4]
for i in range(len(array))[::-1]:
    for j in range(i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print array


for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
            array[i],array[j]=array[j],array[i]
print array

def cmp(s1,s2):
    if s1<s2:
        return 1
    if s1>s2:
        return -1
    else:
        return 0    
