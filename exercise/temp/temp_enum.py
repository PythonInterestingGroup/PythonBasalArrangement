
from enum import Enum,unique

Weekday = Enum('Week',('MON','TUE','WEN','THU','FRI','SAT','SUN'))

for name,member in Weekday.__members__.items():
	print(name,'==>',member,',',member.value)
	
@unique
class SEASON(Enum):
	SPR = 0
	SUM = 1
	AUT = 2
	WIN = 3

season1 = SEASON.SUM
print(season1)
	