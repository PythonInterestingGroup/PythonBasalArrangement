# -*- codeing: utf-8 -*-

#类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Student1(object):
    pass

bart=Student1()
print(bart)  #<__main__.Student object at 0x00469550>指向Student的一个实例
print(Student1)  #<class '__main__.Student'>

#可以自由的给实例变量绑定属性
bart.name='Bart'
print(bart.name)

#由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
#__init__方法的第一个参数永远是self，表示创建的实例本身
#创建变量时，self不需要传，Python解释器自己会把实例变量传进去
class Student2(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
bart=Student2('Bart',60)
print('%s:%s'%(bart.score,bart.name))

#打印学生成绩
#在上面的Student类中，每个实例就拥有各自的name和score这些数据
#要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法
class Student3(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
#定义一个方法，除了第一个参数是self外，其他和普通函数一样，self不用传递，其他参数正常传入：
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
bart=Student3('Bart',60)
bart.print_score()

#封装的另一个好处是可以给Student类增加新的方法
class Student4(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
#定义一个方法，除了第一个参数是self外，其他和普通函数一样，self不用传递，其他参数正常传入：
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    def get_grade(self):
        if self.score>=90:
            return 'A'
        if self.score>=60:
            return 'B'
        else:
            return 'C'
bart=Student4('Bart',60)
print(bart.get_grade())

#让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
#实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student5(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
#外部获取变量
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
#外部修改变量
    def set_score(self, score):
        self.__score = score
#修改变量值可做参数检查
    def set_score1(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student5('Bart Simpson', 98)

#print(bart.__name)
# #无法从外部访问实例变量.__name和实例变量.__score
