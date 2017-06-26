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
#URLError是OSError的一个子类，HTTPError是URLError的一个子类
#如果想用HTTPError和URLError一起捕获异常，那么需要将HTTPError放在URLError的前面.如果URLError放在前面。出现HTTP异常会先响应URLError，这样HTTPError就捕获不到错误信息了

