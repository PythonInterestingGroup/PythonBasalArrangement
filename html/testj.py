# -*- coding: utf-8 -*-
import requests
import json
import os
import time
import sys
KEY='70a315f07d324b3ea02cf21d13796605'
def restart_program():
    print ('restart')
    python = sys.executable
    os.execl(python, python, * sys.argv)

def answerQ(question):
    apiUrl='http://www.tuling123.com/openapi/api'
    print (apiUrl)
    data={'key':KEY,'info':question,'userid':'qq1'}
    # try:
    payload = {'key':KEY,'info':question}
    try:
        r=requests.post(apiUrl,data=payload)
        print (r.text)
        mytext = json.loads(r.text)
        return mytext['text']
    except Exception as e:
        print (e)
        restart_program()
        return 'bug'
if __name__ == "__main__":

    print (answerQ('北京天气'))
