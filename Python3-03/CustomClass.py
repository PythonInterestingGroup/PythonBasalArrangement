# _*_ coding: utf-8 _*_


class Student(object):
	def __init__(self ,name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)'%self.name
	repr == __str__

print(Student('Micoal'))
s = Student('nico')
print(s)

#iter() 返回类对象的Iterator 不断地调用类对象的 next() 方法
class Fibs(object):
	def __init__(self):
		self.a, self.b = 0, 1 #初始化两个计数器 a, b

	def __iter__(self):
		return self  #实例本身就是迭代对象, 故返回自己

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b #计算下一个值
		if self.a > 100000:
			raise StopIteration()
		return self.a #返回下一个值

fibs = Fibs()
for n in fibs:
	print(n)

#__getitem__ 可以像 list 一样取出指定元素 iter()不行

class SubFib(Fibs):
	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a+b
		return a 

f = SubFib()
print("f[10] =",f[10])

class ReSubFib(Fibs):
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a+b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x > start:
					L.append(a)
				a, b = b, a+b
			return L

f2 = ReSubFib()
print("f2[10] =",f2[10])
print("f2[0:5] =",f2[0:5])
		 
# __getattr__ 动态返回一个属性 已存在的属性不会在 getattr 中查找
class SubStudent(Student):
	def __getattr__(self, attr):
		if attr == "score":
			return 99
		if attr == "age":
			return lambda : 25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s2 = SubStudent("mico")
print("score = %s"%s2.score)
print("age()=%s"%s2.age())

# example :  REST API URl 实现完全动态
class Chain(object):

	def __init__(self, path = ''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s'%(self._path,path))
	def __str__(self):
		return self._path
	repr = __str__
print(Chain().status.user.timeline.list)

# __call__

class Stu(object):
	def __init__(self, name):
		self.name = name

	def  __call__(self):	
		print("My name is %s."%self.name)

st = Stu("meico")
print(st())
# 使用 Callable() 来判断一个对象是否可调用









