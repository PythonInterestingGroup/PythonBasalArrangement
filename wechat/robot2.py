# coding:utf-8
class Robot(object):
	"""docstring for Robot"""
	def __init__(self,name,position,direction):
		super(Robot, self).__init__()
		self.name=name
		self.position=position
		self.direction=direction
	def print_position(self):
		print self.position
	def turnRight(self):
		self.direction=self.direction+1 if self.direction<3 else 0
	def turnLeft(self):
		self.direction=self.direction-1 if self.direction>0 else 3
	def moveUp(self):
		if self.direction==1:
			self.position=(self.position[0],self.position[1]+1)
		else:
			print '方向错误'
	def moveDown(self):
		if self.direction==3:
			self.position=(self.position[0],self.position[1]-1)
		else:
			print '方向错误'
	def moveLeft(self):
		if self.direction==0:
			self.position=(self.position[0]-1,self.position[1])
		else:
			print '方向错误'
	def moveRight(self):
		if self.direction==2:
			self.position=(self.position[0]+1,self.position[1])
		else:
			print '方向错误'

r=Robot('myRobot',[0,0],1)

def touHenTie(r,aim):
	print r.position
	while r.position[0]<aim[0]:
		while r.direction!=2:
			r.turnRight()
			print '向右转'
		r.moveRight()
		r.print_position()
	while r.position[1]<aim[1]:
		while r.direction!=1:
			r.turnRight()
			print '向右转'
		r.moveUp()
		r.print_position()
	else:
		print '到达'


touHenTie(r,[4,2])

