# 见 5.22 提交
# 
students =[('john','B',15),('jane','A',12),('dave','B',10),('ethan','C',20),('peter','B',20),('mike','C',16)]
result = sorted(students, key=lambda student:(student[1],-student[2]))
print(result)