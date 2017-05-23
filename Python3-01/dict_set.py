# _*_ coding:utf-8 _*_

d = {'Micheal': 95, 'Bob': 75, 'Tracy': 100}
print("d = ",d)
print("d['Bob']=%s, 要避免key不存在的错误: \n1.通过 key in dict 判断\n 2.dict.get('Bob', value)不存在时返回指定 value"%d['Bob'])
print("要删除一个 key, 使用pop(key)方法")


s = set([1, 1, 2, 2, 3, 3])
print("s = {[1, 1, 2, 2, 3, 3]}, s = %s,可见重复元素在set中自动过滤"%s)
print("add(key)添加元素, remove(key)方法删除元素.set可以看成数学意义上的无序和无重复元素的集合")
s1 = set([1, 2, 3])
s2 = set([2, 3, 6])
print("s1 & s2 =",s1 & s2)
print("s1 | s2 =",s1 | s2)


list1 = [1, 2, 5, 6, 7, 90, 34, 25, 87, 55]
s4 = set(list1)
print("lsit = ",list1)
d[list1] = "123"
print("dict[list] =  ",d)
s4.remove(1)
s4.add(998)
print("s4 = ",s4)
t = ('tuple1','tuple2')
print("tuple = ",t)