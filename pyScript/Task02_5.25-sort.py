# --*-- coding:utf-8 --*--
students = [('john','B',15), ('jane','A',12), ('dave','B',10), ('ethan','C',20), ('peter','B',20), ('mike','C',16)]

def comp(column, listSeq, index):
    if listSeq[index][column] >= listSeq[index+1][column]:
        tmp = listSeq[index+1]
        listSeq[index+1] = listSeq[index]
        listSeq[index] = tmp

for i in range(0, len(students)-1):
    comp(1, students, i)

print students

for i in range(0, len(students)-1):
    comp(2, students, i)
print students

print sorted(students, key = lambda student:student[1])

print sorted(students, key = lambda student:student[2])
#print students
