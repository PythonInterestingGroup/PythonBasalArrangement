# coding:utf-8
import requests
from lxml import html
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    'Cookie': 'q_c1=ecd961b22c784aa1823325ccd5997ec9|1495006205000|1453884576000; __utma=51854390.975736868.1453884578.1477359604.1495006214.5; __utmv=51854390.000--|2=registration_date=20150116=1^3=entry_date=20160127=1; d_c0="AFCAvMqevQqPTnTp0qLbFQEmGk9jAclHtcM=|1477303893"; _zap=65419f24-30dd-41bb-a2fa-bbfda857ed37; aliyungf_tc=AQAAAHdJNTYeLAQAmsxgyvV6KG4PT2UH; acw_tc=AQAAAKWdrAHMXAUAmsxgyryNy0VfAlec; _xsrf=2|da626799|4130a50cd04a88d8783d55c0bc6f70a6|1495006188; XSRF-TOKEN=2|39c366b1|a291a42433eb89f09b9c54e85fce718e|1495006188; l_n_c=1; r_cap_id="NWIzMmQxMjUxMzE2NGQxMWE5NmE3MGRlZWM1NjYzYTg=|1495006205|46cbbe623fc2e1ad42e3a58b8db0bb6c6360992d"; cap_id="YzA5ZDk0ZjU5ZmE5NDU2YjhiYmM1MDI1Njg3OTY3MDE=|1495006205|19594b760d2b4542883f977f57529f72d7a69ff4"; __utmb=51854390.0.10.1495006214; __utmc=51854390; __utmz=51854390.1495006214.5.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); z_c0=Mi4wQUZEQ1QzOUtmQWNBVUlDOHlwNjlDaGNBQUFCaEFsVk5CWWxEV1FBbHFROWl4clJOTHZxdGd4X2prQkJBWWFIa1Vn|1495006213|794778f00b32ef76b42dbb597aecedbee797730b',   # 你的cookie
    'Host': 'www.zhihu.com',
    'Connection': 'keep-alive',
}


def get_link_ist(collection_num):
    page = input('你想要多少页？(注意身体哦～):')
    result = []
    collection_title = None
    for i in range(1, int(page)+1):
        link = 'https://www.zhihu.com/collection/{}?page={}'.format(collection_num, i)
        response = requests.get(link, headers=headers).content
        sel = html.fromstring(response)
        # 创建文件夹
        if collection_title is None:
            # 收藏夹名字
            collection_title = sel.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()')[0].strip()
            if not os.path.exists(collection_title):
                os.mkdir(collection_title)
        each = sel.xpath('//div[@class="zm-item"]//div[@class="zm-item-answer "]/link')
        for e in each:
            link = 'https://www.zhihu.com' + e.xpath('@href')[0]
            print(link)
            result.append(link)
    return [collection_title, result]


def get_pic(collection, answer_link):
    response = requests.get(answer_link, headers=headers).content
    print(response)
    sel = html.fromstring(response)
    title = sel.xpath('//h1[@class="QuestionHeader-title"]/text()')[0].strip()
    try:
        # 匿名用户
        author = sel.xpath('//a[@class="UserLink-link"]/text()')[0].strip()
    except:
        author = u'匿名用户'
    # 新建路径
    path = collection + '/' + title + ' - ' + author
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        n = 1
        for i in sel.xpath('//div[@class="RichContent-inner"]//img/@src'):
            # 去除whitedot链接
            if 'whitedot' not in i:
                # print i
                pic = requests.get(i).content
                fname = path + '/' + str(n) + '.jpg'
                with open(fname, 'wb') as p:
                    p.write(pic)
                n += 1
        print(u'{} 已完成'.format(title))
    except :
        pass


if __name__ == '__main__':
    # https://www.zhihu.com/collection/69135664
    # 收藏夹号码就是：69135664
    collection_num = input('输入收藏夹号码：')
    r = get_link_ist(collection_num)
    collection = r[0]
    collection_list = r[1]
    for k in collection_list:
        get_pic(collection, k)
