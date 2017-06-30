# -*- coding: utf-8 -*-
#author dm

#有道翻译

from urllib import request
from urllib import parse
import json

if __name__=='__main__':
    #Request_URL='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=http://www.baidu.com/link'
    Request_URL = 'http://fanyi.youdao.com/translate_o'
    Form_Data={}
    Form_Data['i']='jack'
    Form_Data['from']='AUTO'
    Form_Data['to']='AUTO'
    Form_Data['smartresult']='dict'
    Form_Data['client']='fanyideskweb'
    Form_Data['salt']='1498023497461'
    Form_Data['sign']='a2bfda11561548fe2e7e9ba9e0f3a454'
    Form_Data['doctype']='json'
    Form_Data['version']='2.1'
    Form_Data['keyfrom']='fanyi.web'
    Form_Data['action']='FY_BY_CLICKBUTTON'
    Form_Data['typoResult']='true'

    data = parse.urlencode(Form_Data).encode('utf-8')   #使用urlencode方法转换标准格式
    response = request.urlopen(Request_URL, data)
    html=response.read().decode('utf-8')
    translate_results=json.loads(html)
    print("结果是：%s" % translate_results)
    translate_results=translate_results['translateResult'][0][0]['tgt']  #找到翻译结果
    print("翻译的结果是：%s" % translate_results)

    #{"translateResult":[[{"tgt":"杰克","src":"jack"}]],"errorCode":0,"type":"en2zh-CHS","smartResult":{"entries":["","n. 千斤顶；[电] 插座；男人\r\n","adj. 雄的\r\n","vt. 增加；提醒；抬起；用千斤顶顶起某物\r\n"],"type":1}}

