# coding:utf-8
import os
import sys
import itchat
import re
reload(sys)
sys.setdefaultencoding( "utf-8" )
itchat.login()
friendList=itchat.get_friends(update=True)[0:]
# print friendList
# path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]  
# fo=open('%s/wechat.txt'%(path),'w')
# # for f in friendList:
# 	# fo.write(str(f)+'\n')

# male = female = other = 0

# for i in friendList[1:]:
#     sex = i["Sex"]
#     if sex == 1:
#         male += 1
#     elif sex == 2:
#         female += 1
#     else:
#         other += 1
#         fo.write(str(i['NickName'])+'\n')

# # 总数算上，好计算比例啊～
# total = len(friendList[1:])
# fo.close()

# # 好了，打印结果
# print u"男性好友：%.2f%%" % (float(male) / total * 100)
# print u"女性好友：%.2f%%" % (float(female) / total * 100)
# print u"其他：%.2f%%" % (float(other) / total * 100)
	


# from echarts import Echart, Legend, Pie

# chart = Echart(u'%s的微信好友性别比例' % (friendList[0]['NickName']), 'from WeChat')
# chart.use(Pie('WeChat',
#               [{'value': male, 'name': u'男性 %.2f%%' % (float(male) / total * 100)},
#                {'value': female, 'name': u'女性 %.2f%%' % (float(female) / total * 100)},
#                {'value': other, 'name': u'其他 %.2f%%' % (float(other) / total * 100)}],
#               radius=["50%", "70%"]))
# chart.use(Legend(["male", "female", "other"]))
# del chart.json["xAxis"]
# del chart.json["yAxis"]
# chart.plot()

for i in friendList:
# 获取个性签名
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
# 正则匹配过滤掉emoji表情，例如emoji1f3c3等
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    print signature