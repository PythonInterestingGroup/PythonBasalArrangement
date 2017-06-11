# --*-- coding: utf-8 --*--
"Convert the names with the first letter been uppercase and the remained been lower-case"

def convertName(name):
	return name[0].upper() + name[1:].lower()

names = ['adam', 'LISA', 'barT']

print map(convertName, names)