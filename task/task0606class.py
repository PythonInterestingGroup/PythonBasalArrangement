# -*- codeing: utf-8 -*-

class Robot(object):
    def __init__(self,name,position,towards,):
        self.__name=name
        self.__position=position
        self.__toward=towards

    def get_name(self):
        return self.__name
    def get_position(self):
        return  self.__position
    def get_toward(self):
        return self.__toward

    def set_name(self,name):
        self.__name = name
    def set_position(self,position):
        self.__position = position
    def set_toward(self,towards):
        self.__toward = towards

#提供 向左转 向右转 方法，每次调用改变机器人朝向
    direction = ['left','top','right','bottom']
    def turn_left(self):
        if self.__toward == 'self':
            self.set_toward('bottom')
        if self.__toward == 'bottom':
            self.set_toward('right')
        if self.__toward=='right':
            self.set_toward('top')
        if self.__toward == 'top':
            self.set_toward('left')
    def turn_right(self):
        if self.__toward=='left':
            self.set_toward('top')
        if self.__toward=='top':
            self.set_toward('right')
        if self.__toward=='right':
            self.set_toward('bottom')
        if self.__toward == 'bottom':
            self.set_toward('left')
#提供 向上移动一步、向下移动一步、向左移动一步、向右移动一步的方法，只有机器人朝向某个方向时才能往该方向移动（如：面朝左边时，只能向左移动，此时如果想向上移动，需要先向右转）
    def move_top(self):
        if self.__toward=='top':
            self.__position[1]+=1
        else:
            self.set_toward('top')
            self.__position[1] += 1
    def move_bottom(self):
        if self.__toward == 'bottom':
            self.__position[1]=self.__position[1]-1
        else:
            self.set_toward('bottom')
            self.__position[1] = self.__position[1] - 1

    def move_left(self):
        if self.__toward == 'left':
            self.__position[0]=self.__position[1]-1
        else:
            self.set_toward('left')
            self.__position[0] = self.__position[1] - 1

    def move_right(self):
        if self.__toward == 'right':
            self.__position[0] += 1
        else:
            self.set_toward('right')
            self.__position[0] += 1

     #打印当前坐标
    def print_position(self):
        print('当前坐标为：',self.__position)

#创建一个机器人，移动到（4，2）的位置，途径（2，6）
name=input('please input your name')
robot1=Robot(name,[0,0],'top')
for i in range(0,6):
    robot1.move_top()
    robot1.print_position()
for j in range(0,4):
    robot1.move_right()
    robot1.print_position()
for x in range(0,4):
    robot1.move_bottom()
    robot1.print_position()


