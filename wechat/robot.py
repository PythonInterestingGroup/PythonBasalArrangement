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
while 1:
	pass
	a=input('Control your robot with "4← 5↓ 6→ 8↑,and 1 to turn left and 3 to turn right\n')
	if a==1:
		r.turnLeft()
	elif a==3:
		r.turnRight()
	elif a==8:
		r.moveUp()
	elif a==5:
		r.moveDown()
	elif a==4:
		r.moveLeft()
	elif a==6:
		r.moveRight()
	r.print_position()


	







