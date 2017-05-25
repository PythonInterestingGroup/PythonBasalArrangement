

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		super(Student, self).__init__()
		self.name = name
		self.score = score

	def print_score(self):
		print("%s:%s"%(self.name,self.score))
		