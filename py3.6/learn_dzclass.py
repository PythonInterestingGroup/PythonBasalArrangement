# -*- coding: utf-8 -*-
#author dm

#定制类
#看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

#__str_
class Student(object):
    def __init__(self,name):
        self.name=name
print(Student('Michael'))  #<__main__.Student object at 0x004C9550>

class Student1(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
print(Student1('Michael'))  #Student object (name: Michael)
s=Student1('Michael')
print(s)  # #Student object (name: Michael)
#直接敲变量不用print，打印出来的实例还是不好看
#这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

#__iter__
#一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1 # 初始化两个计数器a，b
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b  # 计算下一个值
        if self.a >1000:  # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
for n in Fib():
    print(n)

#__getitem__
#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
#Fib()[5]
#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib1(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f=Fib1()
print(f[0])
#list 有个切片对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f2=Fib2()
print(f2[0:5])
#但是没有对step参数作处理：
# >>> f[:10:2]
#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
#此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
#与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
#总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

#__getattr__
#正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
class Student2(object):
    def __init__(self):
        self.name='Bob'
s2=Student2()
print(s2.name)
#print(s2.score)  报错
#要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性
class Student3(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr=='score':
            return 99
s3=Student3()
print(s3.name)
print(s3.score)

class Student4(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
s4=Student4()
print(s4.age)#返回函数<function Student4.__getattr__.<locals>.<lambda> at 0x00784C00>
print(s4.age()) #25

class Student5(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s5=Student5()
print(s5.age())
#print(s5.name)

#无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
print(Chain().status.user.timeline.list)
#还有些REST API会把参数放到URL中,调用时，需要把:user替换为实际用户名
#print(Chain().users('michael').repos)
#不懂

#__call__
#一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用
#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
class Student5(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)
s5= Student5('Michael')
print(s5()) # self参数不要传入，My name is Michael.
#__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
#如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
#我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
print(callable(Student5('bob')))
print(callable(max))
print(callable([1, 2, 3])) #F
print(callable(None)) #F
print(callable('str')) #F

####内容太多 有待消化



