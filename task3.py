a      = ['liangjianghao is hansome','xiongyue is single dog','pangruo is gaygayde']
result = {}
for s in a:
   for char in s:
      result[char] = result.get(char,0) + 1
print(result)	  
