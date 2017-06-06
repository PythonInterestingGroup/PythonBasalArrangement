# coding:utf-8
import itchat
# 注册消息响应事件，消息类型为itchat.content.TEXT，即文本消息
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])

# @itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
  # 返回同样的文本消息
  # return msg['Text']
  	# print msg['url']
  	for key in msg:
  		print key
  		print msg[key]

	print msg['Url']
	itchat.send(msg['Url'],toUserName='filehelper')
itchat.auto_login(True)
# 绑定消息响应事件后，让itchat运行起来，监听消息
itchat.run()