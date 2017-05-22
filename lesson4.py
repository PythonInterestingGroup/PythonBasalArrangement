class Myclass:
    name='sam'

def sayhi(self):
    print 'hello %s'%self.name

mc=Myclass()
print mc.name
mc.name='lily'
mc.sayhi()
