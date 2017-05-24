# _*_ coding:utf-8 _*_


a = ['liangjianghao is hansome','xiongyue is single dog','pangruo is gaygayde']
n = 0
count = {}
for s in a :
	for ch in s:
		if ch in count:
			n = count[ch]
			count[ch] = n + 1
		else :
			n = 0
			count[ch] = 1
		
print(count)