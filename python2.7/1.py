# -*- coding: utf-8 -*-
#构造get参数
#zipcode = sys.argv[1]
wd = input("search word:")
data = urllib.urlencode([('wd',wd)])

#构造url 拼接请求参数
url= "http://www.baidu.com"
url = url + "?" + data
print 'ursing url', url

#构造request 并请求
req = urllib2.Request(url)
fd = urllib2.urlopen(req)

#读取相应结果
while True:
    data = fd.read(1024)
    if not len(data):
        break
    #sys.stdout.write(data)
    print data