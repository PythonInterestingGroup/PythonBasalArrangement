# _*_ coding: utf-8 _*_


#匿名函数
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。

#计算f(x)=x*x
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#lambda x: x * x
def f(x):
    return x*x

#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

#匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x * x
print(f)
print(f(5))

#也可以把匿名函数作为返回值返回
def build(x,y):
    return lambda: x * x + y * y


#lambda:x+y lambda里面没有参数，所以x， y是函数里面定义的x，y
def fn1():
    x, y = 1, 2
    return lambda:x+y
print(fn1()())  #3

#lambda x，y：x+y 调用需要两个参数x,y
def fn2():
    x, y = 1, 2
    return lambda x,y:x+y
print(fn2()(3,4))  #7

#lambda x=x，y=y：x+y
def fn3():
    x, y = 1, 2
    # 或者lambda m = x，n = y:m+n
    return lambda x = x,y = y:x+y
print(fn3()())  #3
print(fn3()(3,7))  #10

#limbda里面定义了m和n，再将x，y分别赋值给m和n,调用可传可不传参数
