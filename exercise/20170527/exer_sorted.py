###
L1 = [12,34,-21,45,-63,1,2,4]
L2 = sorted(L1);
L3 = sorted(L1,key=abs)

print("L1:",L1)
print("L2:",L2)
print("L1:",L3)

L4 = ["Asgs","sfag","Zdfa","dsaf"]
L5 = sorted(L4,key = str.lower)
L6 = sorted(L4,key = str.lower,reverse = True)

print("L4:",L4)
print("L5:",L5)
print("L6:",L6)

L7 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88),('Lisa', 98)]
L8 = sorted(L7,key = lambda value : value[0])
L9 = sorted(L7,key = lambda value : (value[0] , -value[1]))

print("L7:",L7)
print("L8:",L8)
print("L9:",L9)

