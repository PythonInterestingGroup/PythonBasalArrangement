# -*- conding:UTF-8 -*-
from urllib import request
from urllib import error

if __name__ == "__main__":
    url = "http://www.douyu.com/ursus.html"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
        html = response.read().deconde('utf-8')
        print(html)
    except error.URLError as e:
        print(e.reason)
    finally:
        print("end...")