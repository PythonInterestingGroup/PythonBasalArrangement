### 高级特性
from collections import Iterable  

## 切片
print('--------------------- ')
L1 = ['class','interface','method','field','package']

print(L1)
print (L1[:3])
print (L1[-3:])

L2 = list(range(100))
print (L2[:10])

## 每隔多少个取一个
print (L2[:50:5])

T1 = tuple(range(10))
print(T1[0:8:2])

str1 = "I've got you in my sight"
print (str1[:3])

str2 = "我看到你们了"
print(str2[:3])
print(str2.encode('utf-8'))
print(str2.encode('utf-8')[:3])  


## 迭代
L3 = list(range(20))
def connList():
	str1 = ''
	for n in L3 :
		str1 += str(n)
	return str1
print (connList())

D1 = {'76':25,'reaper':8,"roadhog":4}
print(D1)
print(D1.items())
print(isinstance(D1.items(), Iterable))

for key in D1 :
	print(key,':',D1.get(key))
	
for key,value in D1.items() :
	print(key,'-',value)
	
for i,value in enumerate([1,23,5,63]):
	print(i,':',value)
	
for x,y,z in [(1,2,3),(1,4,6),(3,4,5)]:
	print(x,y,z)
print(type((1,2,3,4,5)))
print(type(D1.items()),D1.items())
print(type(enumerate([1,23,5,63])),enumerate([1,23,5,63]))

