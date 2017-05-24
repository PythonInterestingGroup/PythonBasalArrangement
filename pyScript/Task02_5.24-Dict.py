# --*-- coding:utf-8 --*--

a = ['liangjianghao is hansome','xiongyue is single dog','pangruo is gaygayde']

letters = 'abcdefghijklmnopqrstuvwxyz'
letterNums = {}

for i in range(0, len(letters)):
    #tmpNum = a[].count(letters[i])
    tmp = [a[j].count(letters[i]) for j in range(0, len(a))]
    tmpNum = tmp[0] + tmp[1] + tmp[2]
    letterNums[letters[i]] = tmpNum

print letterNums
