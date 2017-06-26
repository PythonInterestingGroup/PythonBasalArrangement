from urllib import  request
from urllib import error

if __name__ == '__main__':
    url = 'http://www.iloveyou.com/' #tan90
    req = request.Request(url)
    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        print(html)
    except error.URLError as e:
        print(e.reason)


