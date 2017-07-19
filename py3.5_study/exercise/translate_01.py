#!/usr/bin/env python
#-*- coding:utf-8 -*-
from urllib import request
from urllib import  parse
import  json

if __name__=='__main__':
    request_URL='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link'
    form_Data ={}
    form_Data['i'] = 'jack'
    form_Data['from'] = 'AUTO'
    form_Data['to'] = 'AUTO'
    form_Data['smartresult'] = 'dict'
    form_Data['client'] = 'fanyideskweb'
    form_Data['salt'] = '1498013814164'
    form_Data['sign'] = '98fbf0c7558f81fb2469ea3e51951ca9'
    form_Data['doctype'] = 'json'
    form_Data['version'] = '2.1'
    form_Data['keyfrom'] = 'fanyi.web'
    form_Data['action'] = 'FY_BY_ENTER'
    form_Data['typoResult'] = 'true'
    #使用urlencode方法转换标准格式
    data = parse.urlencode(form_Data).encode('utf-8')
    # 传递Request对象和转换完格式的数据
    response = request.urlopen(request_URL,data)
    #读取信息并解码
    html = response.read()
    html = html.decode('utf-8')
    #使用json
    translate_results = json.loads(html)
    #找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    #打印翻译结果
    print("结果:%s" % translate_results)
