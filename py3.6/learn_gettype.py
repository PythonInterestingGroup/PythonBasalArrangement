# -*- coding: utf-8 -*-
#author dm

#type() 判断对象类型
#基本类型
print(type(124))  #<class 'int'>
print(type('abc'))  #<class 'str'>
print(type(None))  #<class 'NoneType'>

#函数或者类
print(type(abs))  #<class 'builtin_function_or_method'>

print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==type('123'))
print(type('abc')==str)
print(type('abc')==type(123)) #false

#判断一个对象是否是函数
import types
def fn():
    pass
#true
type(fn)==types.FunctionType
type(abs)==types.BuiltinFunctionType
type(lambda x: x)==types.LambdaType
type((x for x in range(10))) == types.GeneratorType

isinstance('a', str)
#是否为变量中的一种
isinstance([1, 2, 3], (list, tuple))

#dir()
#获得一个对象的所有属性和方法
print(dir('abc'))

#类似__xxx__的属性和方法在Python中都是有特殊用途的，调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
#等价
print(len('abc'))
print("abc".__len__())

#我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法
class Mydog(object):
    def __len__(self):
        return 100
dog=Mydog()
len(dog)

#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class Myobject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

obj=Myobject()

#测试对象的属性
print( hasattr(obj, 'x')) #有属性‘X’吗
print(obj.x)

print(hasattr(obj,'y')) #有属性‘y’吗
setattr(obj,'y',19)  #设置属性‘y’
print(hasattr(obj,'y'))  #有属性‘y’吗
print(getattr(obj,'y'))  #获取属性‘y’
print(obj.y)    #获取属性‘y’

#print(getattr(obj,'z'))  #获取不存在的属性，会抛出AttributeError的错误
print(getattr(obj,'z',404)) # 获取属性'z'，如果不存在，返回默认值404
print(getattr(obj,'x',404))

#也可获取对象的方法
print(hasattr(obj,'power')) #有属性‘power’吗
print(getattr(obj,'power')) # 获取属性'power'
fn=getattr(obj,'power') # 获取属性'power'并赋值到变量fn
print(fn)      #fn指向obj.power
print(fn())   # 调用fn()与调用obj.power()是一样的
print(obj.power())

#通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。
#如果可以直接写：
#sum = obj.x + obj.y
#就不要写：
#sum = getattr(obj, 'x') + getattr(obj, 'y')

#正确的例子
#我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场
def readImage(fp):
    if hasattr('fp','read'):
        return  readData(fp)
    return None


#由于Python是动态语言，根据类创建的实例可以任意绑定属性。
#给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    def __init__(self,name):
        self.name=name
s=Student("Bob")
s.score=90

#类属性，可以直接在class中定义属性，归类所有
class Student1(object):
    name='Student'
#类属性虽然归类所有，但类的所有实例都可以访问到
s=Student1()
print(s.name)   # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student1.name)  # 打印类的name属性
s.name='Michael'  # 给实例绑定name属性
print(s.name)   # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
del s.name  # 如果删除实例的name属性
print(s.name)    # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了






