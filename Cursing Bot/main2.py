import nltk
from chatterbot.trainers import ListTrainer # chatbot 훈련시키는 방법
from chatterbot import ChatBot # import the chatbot
import os

bot = ChatBot('Test') # chatbot 만들기

conv = open('fuck.txt', 'rt', encoding='utf-8').readlines()

trainer = ListTrainer(bot)

trainer.train(conv)

while True:
    request = input('You: ')
    response = bot.get_response(request)

    print('Bot: ', response)

# 테스트 코드임 main.py가 찐코드