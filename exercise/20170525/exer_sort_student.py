##

students = [('john','B',15),('jane','A',12),('dave','B',10),('ethan','C',20),('peter','B',20),('mike','C',16)]

def compareStudent(stu1) :
	return (stu1[1],-stu1[2])
	
r1 = sorted(students, key = compareStudent)
print(r1)

#r2 = sorted(students, key=lambda stu:(stu[1],-stu[2]))
#print(r2)