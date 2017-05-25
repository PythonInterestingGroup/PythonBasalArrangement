# -*- coding:UTF-8 -*-
lst = ['liangjianghao is handsome', 'xiongyue is a single dog', 'pangruo is gaygayde']
dict1 = {}
for i in lst:
    i = i.replace(' ', '')  # 去除空格
    for letter in i:
        if letter in dict1.keys():
            dict1[letter] = dict1[letter] + 1
        else:
            dict1[letter] = 1
print(dict1)
