#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      loretta
#
# Created:     26/05/2017
# Copyright:   (c) loretta 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from operator import itemgetter

if __name__ == '__main__':
    students =[('john','B',15),
 ('jane','A',12),
 ('dave','B',10),
 ('ethan','C',20),
 ('peter','B',20),
 ('mike','C',16)]
    print sorted(students, key=itemgetter(1,2))
