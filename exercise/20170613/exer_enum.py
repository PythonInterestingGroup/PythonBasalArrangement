#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum,unique

Week = Enum('Week',('Mon','Tue','Wed','Thu','Fri','Sat','Sun'))

for name,member in Week.__members__.items():
	print(name,'=>',member,',',member.value)
	
@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu	= 4
	Fri = 5
	Sat = 6
	
print("Weekday.Thu :",Weekday.Thu)
print("Weekday['Fri']:",Weekday['Fri'])
print("Weekday(2):",Weekday(2))
print("Weekday.Tue.value:",Weekday.Tue.value)





