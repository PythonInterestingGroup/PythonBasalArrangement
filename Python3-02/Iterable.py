# _*_ coding: utf-8 _*_

from collections import Iterable
print("[] is ",isinstance([], Iterable))
print("{} is ",isinstance({}, Iterable))
print("str is ",isinstance("str", Iterable))
print("生成式 is ",isinstance((x for x in range(10)), Iterable))
print("100 is ",isinstance(100, Iterable))


print("可以直接作用于 for 循环的对象统称为可迭代对象: Iterable ")
print("可以被 next() 函数调用并不断返回下一个值得对象称为 Iterator")
print("生成器都是 Iterator 对象,但 list, dict,str 虽然是 Iterable, 但不是 Iteraor")
print("Iterator的计算都是惰性的甚至可以表示无限大的数据流,而 list 等不可能")
print("Python 的 for 循环本质就是不断调用 next()")

#首先获得 Iterator 对象
it = iter([1, 2, 3, 4, 5])
while True:
	try:
		#获得下一个值
		x = next(it)
		print(x)
	except StopIteration:
		# 遇到 StopIteration 就退出循环
		break