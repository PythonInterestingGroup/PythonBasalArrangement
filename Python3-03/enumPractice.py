# _*_ coding:utf-8 _*_
from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
	print(name,'==>',member,',',member.value)

 # print(Month.Month.Jan)
@unique
class SEASON(Enum):
	SPR = 0
	SUM = 1
	AUT = 2
	WIN = 3

season1 = SEASON.SUM
print(season1)


