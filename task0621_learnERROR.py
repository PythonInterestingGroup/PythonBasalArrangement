from urllib import  request
from urllib import error

if __name__ == '__main__':
    url = 'http://www.douyu.com/JYWang.html' #tan90
    req = request.Request(url)
    try:
        response = request.urlopen(req)
    except error.URLError as e:
        if hasattr(e,'code'):
            print('HTTPError')
            print(e.code)
        elif hasattr(e,'reason'):
            print('URLError')
            print(e.reason)
#URLError��OSError��һ�����࣬HTTPError��URLError��һ������
#�������HTTPError��URLErrorһ�𲶻��쳣����ô��Ҫ��HTTPError����URLError��ǰ��.���URLError����ǰ�档����HTTP�쳣������ӦURLError������HTTPError�Ͳ��񲻵�������Ϣ��

