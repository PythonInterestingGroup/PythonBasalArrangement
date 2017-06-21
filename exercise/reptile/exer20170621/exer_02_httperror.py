# -*- coding: UTF-8 -*-

from urllib import request
from urllib import error

if __name__ == "__main__":

    url = "http://www.douyu.com/ursus"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
        html = response.read()
        print(html)
    except error.HTTPError as e:
        print(e.code)
    except error.URLError as e:
        print(e.reason)
    finally:
        print("end...")
