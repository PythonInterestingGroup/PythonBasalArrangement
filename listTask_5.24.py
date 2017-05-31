#! /usr/bin/env python3
a = ['liangjianghao is handsome', 'xiongyue is a single dog', 'pangruo is gaygayde']
dic = {}

for item in a:
    for letter in item:
        isExist = letter in dic
        if isExist:
            count = int(dic[letter]) + 1
            dic[letter] = count
        else:
            if letter != ' ':

                dic[letter] = 1
print(dic)

# 有没有比双层遍历更好的方法??
