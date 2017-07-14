
# -*- coding: utf-8 -*-

from urllib import  request
from  urllib import parse
import  json

if __name__ == '__main__':
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

    form_data = {}
    form_data['i'] = '瘦子'
    form_data['type'] = 'AUTO'
    form_data['doctype'] = 'json'
    form_data['xmlVersion'] = '1.8'
    form_data['keyfrom'] = 'fanyi.web'
    form_data['ue'] = 'UTF-8'
    form_data['action'] = 'FY_BY_CL1CKBUTTON'
   # form_data['typoResult'] = 'true'
    data = parse.urlencode(form_data).encode('utf-8') # 转换标准格式
    response = request.urlopen(url, data)
    html = response.read().decode('utf-8')
    result = json.loads(html)
    print('result = %s' % result)
    result = result["translateResult"][0][0]["tgt"]
    print(" result = %s" % result)