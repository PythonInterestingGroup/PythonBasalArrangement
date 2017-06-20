# -*- coding: UTF-8 -*-

from urllib import request
from urllib import parse
import json

if __name__ == "__main__" :
    Request_Url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link"

    From_Data = {}
    From_Data['i'] = 'python'
    From_Data['from'] = 'AUTO'
    From_Data['to'] = 'AUTO'
    From_Data['smartresult'] = 'dict'
    From_Data['client'] = 'fanyideskweb'
    From_Data['salt'] = '1497975009293'
    From_Data['sign'] = 'ebec239426c6b9949218fb7c3cd55033'
    From_Data['doctype'] = 'json'
    From_Data['version'] = '2.1'
    From_Data['action'] = 'fanyi.web'
    From_Data['smartresult'] = 'FY_BY_CLICKBUTTON'
    From_Data['typoResult'] = 'true'

    data = parse.urlencode(From_Data).encode('utf-8')
    response = request.urlopen(Request_Url,data)
    html = response.read().decode('utf-8')
    print("result:",html)
    translate_result = json.loads(html)
    # print("翻译结果为:%s"%translate_result['translateResult'][0][0]['tgt'])