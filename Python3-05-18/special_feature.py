# _*_ coding: utf-8 _*_

l1 = []
for i in range(10):
	l1.append(i)

# slice 切片 [ a, b) 从a位置到b位置 不包含 b	
print(l1[2:5])

# Iteration 迭代 通过 for in 完成 
d1 = {'a':1, 'b':2 , 'c':3}
for key in d1:
	print(key)

l2 = [(1, 1), (2, 4), (3, 9)]
for key, value in l2:
	print(key, value)
for k, v in d1.items():
	print(k ,"=", v)
#列表生成式 
n1 =  1
print("1到11的偶数的集合 :",[x * x for x in range(1, 11) if x%2==0])
print("123与 abc 的全排列是:",[m+n for m in "123" for n in "abc"])

import os #导入 os 模块
print("当前目录下文件列表:",[d for d in os.listdir('.')])




