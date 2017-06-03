'''
函数的参数:位置参数、默认参数、可变参数、关键字参数、命名关键字参数、参数组合、
'''
# 位置参数
a = pow(5, 2)
print(a)


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


a = power(5, 5)
print(a)
print(power(5))


def enroll(name, gender, age=6, city='shanghai'):
    print('name:', name)
    print('gender:' + gender)
    print('age:%d' % age)
    print('city:', city)


enroll('lipeipei', '女', 7, 'anhui')
enroll('大古', 'man', city='maanshan')  # 当不按顺序提供部分默认参数时，需要把参数名写上
enroll('gyy', 'women', 7)


def add_end(L=[]):
    L.append('end')
    return L


li = add_end([1, 2, 3])
print(li)
li = add_end()
print(li)
lii = add_end()
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，
# 它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
print(lii)


# 计算a^2+b^2+c^2+.......
def cal(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 可变参数
sum1 = cal([2, 3, 4, 6, 7])  # 不变参数
print(sum1)


# *nums表示把nums这个list的所有元素作为可变参数传进去。
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


sum2 = calc(1, 2, 3, 4)
print(sum2)


# 关键字参数
def person(name, age, **kw):
    print('name:', name,
          'age:', age,
          'other:', kw)


person('lpp', 25)
person('gmy', 26, gender='男', city='上海', hobby='play games')

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
extra = {'city': 'shanghai', 'job': 'code monkey ', }
person('jack', 78, city=extra['city'], job=extra['job'])
person('rose', 80, **extra)


# 命名关键字参数:如果要限制关键字参数的名字，就可以用命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


person('gmy', 26, city='上海', job='code monkey')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


f1(1, 2)
f1('1', 'second')
f1(1, 2, 3, 4, '5')
f1(1, 2, 3, 4, 5, X=10, Y=10, Z=100)
f1(1, 5, 2, [1, 2, 3], city='shanghai', gender='男')


# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f2(1, 2, 3, d=12)
f2(1, 2, d=12)
f2(1, 2, 3, d='none', city='shanghai')

# 小结
# 要注意定义可变参数和关键字参数的语法：
#
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
#
# 以及调用函数时如何传入可变参数和关键字参数的语法：
#
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})



