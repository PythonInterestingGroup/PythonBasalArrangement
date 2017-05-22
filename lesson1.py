#print 3/4

from __future__ import division
print 3/4
print 3//4



import re
text ='Hi, i am shirley Hilton.I am his wife'
m=re.findall(r'i.*?e',text)
if m:
    print m
else:
    print 'not match'





position=(1,2)
geeks=('sheldon','leonard','rajesh','howard')
print position[0]
for g in geeks:
    print g
print geeks[1:3]

a='heaven'
b='hell'
c=True and a or b
print c
d=False and a or b
print d




class vehicle:
    def __init__(self,speed):
        self.speed=speed
    def drive(self,distance):
        print 'need %f hours'%(distance/self.speed)

class bike(vehicle):
    pass
class car(vehicle):
    def __init__(self,speed,fuel):
        vehicle.__init__(self,speed)
        self.fuel=fuel
    def drive(self,distance):
        vehicle.drive(self,distance)
        print 'need %f fuels'%(distance/self.fuel)

b=bike(15.0)
c=car(80.0,0.012)
b.drive(100.0)
c.drive(100.0)


class Car:
    speed=0
    def driver(self,distance):
        time=distance/self.speed
        print time

car1=Car()
car1.speed=60.0
car1.driver(100.0)
car1.driver(200.0)
    
car2=Car()
car2.speed=150.0
car2.driver(100.0)
car2.driver(200.0)
    


class Myclass:
    name='sam'

    def sayhi(self):
        print 'hello %s'%self.name
  
mc=Myclass()
print mc.name
mc.name='lily'
mc.sayhi()



class Myclass:
    pass
mc=Myclass()
print mc



s='how old are you'
l=s.split()

dir(s)
dir(list)



cityname=raw_input('''which city's weather do you want to search ''')



import urllib2
web=urllib2.urlopen('http://www.baidu.com')
content = web.read()

f=open('baidu.html','w')
f.write(content)
f.close

print content




from random import randint

name=raw_input('please input your name:')


f=open('c:\Python27\game.txt')
#score=f.read().split()
lines=f.readlines()

scores={}
for i in lines:
    s=i.split()
    scores[s[0]]=s[1:]  #key=s[0] values=[1;] scores[key]=value
score=scores.get(name)
if score is None:
    score=[0,0,0]
    
print score

game_times=int(score[0])
min_times=int(score[1])
total_times=int(score[2])
if game_times>0:
    avg_times=float(total_times)/game_times
else:
    avg_times=0
print 'avgtimes %f'%avg_times

print"%s,you have played %d times,at least %d time get answer,avg times is %.2f"%(
    name,game_times,min_times,avg_times)

num=randint(1,100)
times=0
print 'guess what i think'
bingo=False
while bingo==False:
    times+=1
    answer=input()
    if answer<num:
        print 'too small'
    if answer>num:
        print 'too big'
    if answer==num:
        print 'bingo'
        bingo=True
print 'thistimes %d'%times

if game_times==0 or times<min_times:
    min_times=times

total_times+=times
print 'totaltimes %d'%total_times
game_times+=1
print 'gametimes%d'%game_times

scores[name]=[str(game_times),str(min_times),str(total_times)]
result=''
for n in scores:
    line=n+' '+' '.join(scores[n])+'\n'
    result+=line
    
#result='%d %d %d'%(game_times,min_times,total_times)
    
f=open('game.txt','w')
f.write(result)
f.close()

    




import random
random.randint(1,10)
#random.randchoic([1,3,5])
dir(random)


try:
    f=file('non-exist.txt')

    print 'file opened!'
    f.close()
except:

    print 'file not exists.'

print 'done'

i=0
while i<5:
    i+=1
    for j in range(3):
        print j
        if j==2:
            break
    for k in range(3):
        if k==2:
            continue
        print k
    if i>3:
        break
    print i
    





f=file('score.txt')
lines=f.readlines()
print lines
f.close()

results=[]

for line in lines:
    print line
    data=line.split()
    print data
    
    sum=0
    for score in data[1:]:
        #sum+=int(score)
        point=int(score)
        if point<60:
            continue
        sum+=int(score)
    result='%s\t;%d\n'%(data[0],sum)
    print result

    results.append(result)

output=file('result.txt','w')
output.writelines(results)
output.close()




print 'please input some world'
you=raw_input()
fw=open('write.txt','w')
fw.write(you)
fw.close()



fopen=open('data.txt')
data=fopen.readline()

fwrite=open('output.txt','a')
fwrite.write(data)


#data='i will be in a file.\nso cool!'
#out=open('output.txt','w')
#out.write(data)
#out.close()


# f = file('README.txt')
# data = f.read()
# print data
# f.close()

f = file('data.txt')
data = f.read()
print 'read way'
print data

f = file('data.txt')
data=f.readline()
print 'readline way'
for i in data:
    print i

f=file('data.txt')
data=f.readlines()
print 'reladlines way'
for i in data:
    print i
f.close()





word='hello world'
for c in word:
    print c



from random import choice

score=[0,0]
direction=['left','center','right']

def kick():         #hanshu
    print'===you kick!==='
    print 'choose one side to shoot'
    print 'left,center,right'
    you=raw_input()
    print 'you kicked '+ you
    com=choice(direction)
    print "computer saved "+com
    if you!=com:
        print"Goal!"
        score[0]+=1
    else:
        print 'Oops...'
    print 'score:%d(you)-%d(com)\n'%(score[0],score[1])

    print'===you save!==='
    print 'choose one side to save'
    print 'left,center,right'
    you=raw_input()
    print 'you saved '+you
    com=choice(direction)
    print 'computer kicked '+com
    if you!=com:
        print 'opops...'
        score[1]+=1
    else:
        print 'saved!'
    print 'score:%d(you)-%d(com)\n'%(score[0],score[1])
        
    
for i in range(1):     #xunhuan 1 round
    print '===round %d==='%(i+1)
    kick()

    while(score[0]==score[1]):
        i+=1
        print '===round %d==='%(i+1)
        kick()
    if score[0]>score[1]:
        print 'you win!'
    else:
        print 'you lose.'






from random import choice

score_you=0
score_com=0
direction=['left','center','right']

for i in range(5):
    print '====round %d -you kick!==='%(i+1)  #i shoot
    print 'choose one side to shoot:'
    print 'left,center,right'
    you=raw_input()
    print 'you kiched '+ you
    com=choice(direction)
    print 'computer saved '+com
    if you!=com:
        print 'goal!'
        score_you+=1
    else:
        print 'oops...'
    print 'score:%d(you)-%d(com)\n'%(score_you,score_com)

    print '====round %d -you save!==='%(i+1)   #computer shoot
    print 'choose one side to save:'
    print 'left,center,right'
    you=raw_input()
    print 'you saved '+ you
    com=choice(direction)
    print 'computer kicked '+com
    if you==com:
        print 'saved!'
        
    else:
        print 'oops...'
        score_com+=1
    print 'score:%d(you)-%d(com)\n'%(score_you,score_com)





from random import choice
print 'choose one side to shoot:'
print 'left,center,right'
you=raw_input()
print 'you kiched '+ you
direction=['left','center','right']
com=choice(direction)
print 'computer saved ' + com

if you!=com:
    print 'goal!'
else:
    print 'oops....'
    



def sayhello():     
    print 'hello world'

sayhello()
sayhello()

print bool(-123)
print bool(0)
print bool('abc')
print bool('False')
print bool('')


for i in range(0, 5):
    print'*'

for i in range(0, 5):
    print'*',
print '/n'

for i in range(0, 5):
    for j in range(0, 5):
        print '*',
    print
    
for i in range(0, 5):
    for j in range(0, i+1):
        print '*',
    print
    
    
from random import randint #suijishu
num = randint(1,100)
print 'gusee what i think?'
bingo=False
while bingo==False:
    answer = input()
    if answer<num:
        print '%d is too small!'%answer
    if answer>num:
        print '%d is too big!'%answer
    if answer==num:
    	print 'BINGO! %d is the right answer!'%answer
    	bingo=True



str1='good'
str2='bye'
print str1+' '+str2

print 'very '+str1
print str1+' and '+str2

print 'my age is '+ str(18)
num=18
print 'my age is ' + str(num)
print 'my age is %d'%num


print 'He said,\"i\'m yours!\"'
print '''he sais, "i'm yours!"'''

print '''He said,\"i\'m yours!\"'''

print '\\\\_v_\\\\'
print "\\\\_v_\\\\"
print '''\\\\_v_\\\\'''

print '''Stay hungry,
stay foolish.
-- Steve Jobs'''


print '''*
***
*****
***
*'''

#for i in range(1,4):
#    for j in range(1,i+1):
#        print '*',
#    print '/n'
   






a=1
b=0
while a!=100: 
    b=b+a
    a=a+1
print b



        

num=10
print 'guess what i think?'
answer=input()
if answer<num:
    print 'too small'

if answer>num:
    print 'too big'

if answer==num:
    print 'bingo!'


thisislove = input()
if thisislove:
    print 'abcde'
name = input()
print name


for i in range(1,101):
    print i

