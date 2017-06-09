# #!/usr/bin/python
# # -*- coding: utf-8 -*-
 
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
 
 
# my_bot=ChatBot("Training demo")
# my_bot.set_trainer(ListTrainer)
# my_bot.train([
#     "嗳，渡边君，真喜欢我?",
#     "那还用说?",
#     "那么，可依得我两件事?",
#     "三件也依得",
# ])
 
# # test
# print(my_bot.get_response("真喜欢我?"))
# print(my_bot.get_response("可依得我两件事?"))

# -*- coding: utf-8 -*-
from chatterbot import ChatBot

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

# Get a response to the input text 'How are you?'
response = chatbot.get_response('How are you?')

print(response)