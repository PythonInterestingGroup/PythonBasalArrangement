# _*_ coding:utf-8

from urllib import request
from urllib import  parse
import json

if __name__ == "__main__":
    #对应 request 的 URL
    Request_URL = "http://fanyi.youdao.com/translate_o"
    #创建 Form_Data 字典,存储上图的 Form Data
    Form_Data = {}
    Form_Data["type"] = 'AUTO'
    Form_Data['i'] = 'Jack'
    Form_Data['from'] = "AUTO"
    Form_Data["to"] = "AUTO"
    Form_Data["smartresult"] = "dict"
    Form_Data["salt"] = 1498102055615
    Form_Data["sign"] =	"64d6cd8bd13d87e86389e693e9bac4a7"
    Form_Data['doctype'] = 'json'
    Form_Data['xmlVersion'] = '1.8'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['ue'] = 'ue:UTF-8'
    Form_Data['action'] = 'FY_BY_CLICKBUTTON'
    Form_Data["client"] = 'fanyideskweb'
    #使用 urlencode 方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    #传递 Request 对象和转换完格式的数据
    response = request.urlopen(Request_URL,data)
    #读取信息并解码
    html = response.read().decode('utf-8')
    #使用 json
    translate_results = json.loads(html)
    print('原始 json : %s'%translate_results)
    print("***********************")
    #找到翻译结果
    translate_results = translate_results['translateResult'][0]
    #打印翻译信息
    print("翻译结果是 : %s"%translate_results)

