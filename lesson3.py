num = 10
print 'gusee what i think?'
bingo=False
while bingo==False:
    answer = input()
    if answer<num:
        print 'too small!'
    if answer>num:
        print 'too big!'
    if answer==num:
        print 'BINGO!'
        bingo=True

