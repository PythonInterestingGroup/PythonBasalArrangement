# 变量类型
# 字符串：加号（+）是字符串连接运算符，星号（*）是重复操作
# 变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾
str = 'abcdefghggg23'
print(str)
print(str[0])
print(str[1:-1])
print(str * 3)
str0 = str[0:5]
str1 = str[6:len(str)]
print(str0 * 3 + str1)

# List（列表） 是 Python 中使用最频繁的数据类型
list = [1221, "abdbweh", '155egggde', 4.555, 2356737832847, [123, 1234, '435']]
print(list[5][2])
print(list[4:5])
list[1] = 5566

# 元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ("tery", 1421535, 5216737, 5.888, 'lipeipei')
print(tuple)

# #字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(dict['one'])# 输出键为'one' 的值
print(dict[2])#输出键为2的值
print(tinydict)#输出完整的字典
print(tinydict.keys())#输出所有的键
print(tinydict.values())#输出所有的值

#Python数据类型转换：数据类型的转换，只需要将数据类型作为函数名即可
n = '1234'
type(n)
float(n)
print(n)

