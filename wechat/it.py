# coding:utf-8
import itchat
# 注册消息响应事件，消息类型为itchat.content.TEXT，即文本消息
from qqbot import QQBotSlot as qqbotslot, RunBot

from itchat.content import *

@qqbotslot
def onQQMessage(bot, contact, member, content):
    # if '@ME' in content:
    #     bot.SendTo(contact, )
    # # if content == '-hello':
    # #     bot.SendTo(contact, '你好，我是QQ机器人')
    # elif content == '-stop':
    #     bot.SendTo(contact, 'QQ机器人已关闭')
    #     bot.Stop()
    # print dir(contact)
    bot.SendTo(contact, )
    
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat=True)
def text_reply(msg):
  # 返回同样的文本消息
  # return msg['Text']
  	# print msg['url']
  	# for key in msg:
  		# print key
  		# print msg[key]

	print msg['Url']
	itchat.send(msg['Url'],toUserName='filehelper')



itchat.auto_login(True)
# 绑定消息响应事件后，让itchat运行起来，监听消息
itchat.run()