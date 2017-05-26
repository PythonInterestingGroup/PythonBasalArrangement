### 列表生成式

L1 = []
for x in range(1,12):
	L1.append(x*x)
print("L1:",L1)

## 使用生成式
L2 = [x * x for x in range(1,12)]
L3 = [x * x for x in range(1,30) if x % 2 == 0 or x % 3 == 0]

print("L2:",L2)
print("L3:",L3)

L4 = [x + y for x in 'ABC' for y in 'XYZ']
print("L4:",L4)

T1 = {'x':'A','y':'B','z':'C'}
L5 = [k + '=' + v for k ,v in T1.items()]
L6 = [str(i) + ':' + str(v) for i ,v in enumerate(L2)]
print ("L5:",L5)
print ("L6:",L6)

L7 = [x.lower() for x in L4]
print("L7:",L7)

L8 = [ x.lower() for x in ['A','BQW',12,'wq',21.2] if isinstance(x, str)] 
print("L8:",L8)