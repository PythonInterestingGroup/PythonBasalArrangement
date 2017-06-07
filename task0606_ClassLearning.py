# 创建一个机器人类
# 有姓名，坐标（x坐标和y坐标），朝向(上下左右) 等私有属性
# 初始化时接受一个字符串作为姓名，将坐标初始化在原点（0，0），朝向初始化为 上（y轴正方向）
# 提供 向左转 向右转 方法，每次调用改变机器人朝向
# 提供 向上移动一步、向下移动一步、向左移动一步、向右移动一步的方法，只有机器人朝向某个方向时才能往该方向移动（如：面朝左边时，只能向左移动，此时如果想向上移动，需要先向右转）
# 提供 打印当前坐标 的方法
# 程序要求：创建一个机器人，移动到（4，2）的位置，途径（2，6）

class Robot(object):
    def __init__(self,name,position,direction):
        super(Robot,self).__init__()
        self.name      = name
        self.position  = position
        self.direction = direction
    def get_position(self):
        print(self.position)
    def turnLeft(self):
        self.direction = self.direction - 1 if self.direction > 0 else 3
    def turnRight(self):
        self.direction = self.direction + 1 if self.direction < 3 else 0
    def moveUp(self):
        if self.direction == 1:
            self.position = [self.position[0],self.position[1]+1]
        else:
            print("Try to change your direction first!")
    def moveLeft(self):
        if self.direction == 0:
            self.position = [self.position[0]-1,self.position[1]]
        else:
            print("Try to change your direction first!")
    def moveDown(self):
        if self.direction == 3:
            self.position = [self.position[0],self.position[1]-1]
        else:
            print("Try to change your direction first!")
    def moveRight(self):
        if self.direction == 2:
            self.position = [self.position[0]+1,self.position[1]]
        else:
            print("Try to change your direction first!")

r = Robot('robot001',[0,0],1)
while 1:
    pass
    x = int(input('Please enter 8/4/2/6 for top/left/bottom/right,1,3 for turn left/right:\n'))
    if x == 1:
      r.turnLeft()
    elif x == 3:
      r.turnRight()
    elif x == 8:
      r.moveUp()
    elif x == 4:
      r.moveLeft()
    elif x == 2:
      r.moveDown()
    elif x == 6:
      r.moveRight()
    r.get_position()

