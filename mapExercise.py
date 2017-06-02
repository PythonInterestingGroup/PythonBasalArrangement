name = ['adam','LISA','barT']
def fix(x):
    return x[0].upper()+x[1:].lower()

realName = list(map(fix,name))
print(realName)