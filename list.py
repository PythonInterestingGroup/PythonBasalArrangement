# -*- coding: UTF-8 -*-
# 输出列表
a = ['liangjianghao is hansome', 'xiongyue is single dog', 'pangruo is gaygayde']
print("a[0]:", a[0])
print("a[0:2]", a[1:2])
print(a)

# 更新列表
a[2] = '1992 - 02 - 22'
print(a)

# 删除列表 del
del a[2]
print(a)

# 脚本操作符 + *
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = ['lpp', '1992', '安徽宿州', '双鱼']
list3 = list1 + list2
print(list3)
print(list3 * 3)
print("list3的长度是：", len(list3))

# python列表的函数和方法
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [0, 1, 3, 4, 7, 5, 6]
tuple1 = (1, 2, 3, 4, 5, 6)
print(len(list1))
print(len(list2))
print(max(list1))
print(min(list2))
print(list(tuple1))  # 把元祖转化成列表
list1.append('add')  # 在列表末尾添加元素
print(list1)
print(list1.count('add'))  # list.count(obj),obj是一个元素，返回的是obj在列表中出现的次数
list1.extend(list2)  # list.extend(seq),该方法没有返回值，但会在已存在的列表中添加新的列表内容
print(list1)
print("2首次出现的位置：", list1.index(2))  # list.index(obj):返回对象首次出现的位置索引
list1.insert(0, 'peipei.li')  # list.insert(index,obj):在特定位置插入元素，没有返回值
print(list1)
print(list2.pop())  # 该方法返回从列表中移除的元素对象
print(list2.pop(-1))
list1.remove('peipei.li')  # 该方法没有返回值但是会移除两种中的某个值的第一个匹配项
list1.remove('add')
print(list1)
list1.reverse()  # 该方法没有返回值，但是会对列表的元素进行反向排序
print(list1)
list1.sort()
print(list1)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# Apple:
# 打印Python:
# 打印Lisa:
print(L[0][0])
print(L[1][1])
print(L[2][2])
