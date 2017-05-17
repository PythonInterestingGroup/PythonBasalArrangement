# _*_ coding:utf-8 _*_
# list 和 tuple
classmates = ['jx','lkt','lmd','tjk','ljh']
print("classmates is",classmates)
print('classmates length is %d'%len(classmates))
print('classmates first mermber is %s'%classmates[0])
print('classmates last mermber is %s'%classmates[-1])
classmates.append('xyy')
print("classmates append ",classmates)
classmates.insert(1, 'sxf')
print("classmates insert sxf at index 1",classmates)
classmates.pop(3)
print("classmates pop obj at index 3",classmates)
classmates[3] = 'tfq'
print("classmates replace tfq at index 3",classmates)


#tuple
print("tuple(元组)与 List 相似,但是 tuple 一旦初始化就无法更改\n")
print("tuple 定义时用 t = ('a','b','c'),当 tuple 只有一个元素时, 需要加一个逗号 t = ('a',)")

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print("list L contain : ",L)
print("L[0][0] is ",L[0][0])
print("L[1][1] is ",L[1][1])
print("L[2][2] is ",L[2][2])