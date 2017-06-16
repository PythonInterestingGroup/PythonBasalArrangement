# -*- coding: utf-8 -*-
#author dm

class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('scores must be an integer')
        if value < 0 or value > 100:
            raise ValueError("scores must between 0~100!")
        self._score=value
s=Student()
s.set_score(80)
print(s.get_score())
#s.set_score(101)
print(s.get_score())

#Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student1(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
#把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
s1=Student1()
s.score=60   # OK，实际转化为s.set_score(60)
print(s.score)  # OK，实际转化为s.get_score()
# s.score=999
# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
#birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来
class Student2(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

#练习
#利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution

class Screen(object):
    @property
    def width(self):
        return self._width
#return self.width 会报错
    @width.setter
    def width(self,value):
        self._width=value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value

    @property
    def resolution(self):
        return self._height*self._width

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
