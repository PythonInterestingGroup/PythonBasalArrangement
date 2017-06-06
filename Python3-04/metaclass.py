# _*_ coding:utf-8 _*_

def fn(self, name='world'): #先定义函数
	print("Hello, %s"%name)

#使用 type()创建 Hello class
Hello = type('Hello', (object,),dict(hello=fn))
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

#metaclass 是类的模,所以必须是从 type 类型派生:
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value :self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass = ListMetaclass):
	pass

#加入关键字 meteclass 时,编译器在创建 MyList 时就会调用 ListMetaclass 的
#__new__()方法来创建 __new__()方法接收到的参数一次是:
# 1.当前准备创建的类的对象 
# 2.类名
# 3.类继承的父类集合
# 4.类的方法集合
L = MyList()
L.add(1)
print(L)

x = 1
print("x>1") if x >1 else print("x<=1")