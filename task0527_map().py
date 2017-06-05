list1 = [[1,2,3],[4,5,6],[7,8,9]]
list2 = []
def square(x):
    return x*x
def expand(l):
    for i in l:
        for j in i:
           list2.append(j)
    return list2
print(list(map(square,expand(list1))))
