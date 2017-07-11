# -*- coding: utf-8 -*-
import requests
import json
import os
import time
import sys
KEY='70a315f07d324b3ea02cf21d13796605'
def restart_program():
    print 'restart'
    python = sys.executable
    os.execl(python, python, * sys.argv)

def answerQ(question):
    apiUrl='http://www.tuling123.com/openapi/api'
    print apiUrl
    data={'key':KEY,'info':question,'userid':'qq1'}
    # try:
    payload = {'key':KEY,'info':question}
    try:
        r=requests.post(apiUrl,data=payload)
        print r.text
        mytext = json.loads(r.text)
        return mytext['text']
    except Exception as e:
        print e
        # restart_program()
        return 'bug'
if __name__ == "__main__":

    print answerQ('北京天气')

# def answerQ(question):
#     apiUrl='http://www.tuling123.com/openapi/api'
#     print apiUrl
#     data={'key':KEY,'info':question}
#     print data
#     r=requests.post(apiUrl,data=data).json()
#     print r.get('text')

    # try:
    #     r=requests.post(apiUrl,data=data).json()
    #     print r
    #     print r.get('text')
    #     return r.get('text')
    # except Exception as e:
    #   print e
    #     return
# answerQ('北京天气')
# import json
# url = 'http://www.tuling123.com/openapi/api'
# payload = {'key':'70a315f07d324b3ea02cf21d13796605','info':'北京天气'}
# headers = {'content-type': 'application/json'}

# r = requests.post(url, data=json.dumps(payload), headers=headers)
# print r.text

# import requests

# url = 'http://www.tuling123.com/openapi/api'
# payload = {'key':'70a315f07d324b3ea02cf21d13796605','info':'北京天气'}
# try:
#     r = requests.post(url, data=payload)
#     text = json.loads(r.text)
# except Exception as e:
#     print '超时'

# def answerQ(question):
#     url = 'http://www.tuling123.com/openapi/api'
#     payload = {'key':'70a315f07d324b3ea02cf21d13796605','info':'北京天气'}
#     try:
#         r = requests.post(url, data=payload)
#         text = json.loads(r.text)
#     except Exception as e:
#         print '超时'
#         return '超时'

# print text['text']
# import requests
# url = 'https://api.github.com/some/endpoint'
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print r.text