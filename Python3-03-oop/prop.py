# _*_ coding:utf-8 _*_

class Student(object):

	def score():
	    doc = "The score property."
	    def fget(self):
	        return self._score
	    def fset(self, value):
	    	if value>100 or value < 0:
	    		raise ValueError("score must between 0 ~ 100!")
	    	if not isinstance(value, int):
	    		raise ValueError("score must be an integer!")
	        self._score = value
	    def fdel(self):
	        del self._score
	    return locals()
	score = property(**score())


s = Student()
s.score = 99
print(s.score)

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)