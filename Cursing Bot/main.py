import nltk
from chatterbot.trainers import ListTrainer # chatbot 훈련시키는 방법 chatterbot machine learning api를 활용함
from chatterbot import ChatBot # import the chatbot
import os

bot = ChatBot('Test') # chatbot 만들기


trainer = ListTrainer(bot) # set the trainer

for _file in os.listdir('files'):   # 크롤링한 데이터 파일
    chats = open('files/' + _file, 'rt', encoding='utf-8').readlines() # 한글 파일이므로 utf-8로 인코딩하고 파일에 있는 모든 문자열 리스트를 반환.

    trainer.train(chats)

while True:
    request = input('You: ')
    response = bot.get_response(request)

    if request.strip() != '꺼져':
        response = bot.get_response(request)
        print('Bot: ', response)

    if request.strip() == '꺼져':   # 사용자가 '꺼져'라고 입력하면
        print('Bot: 알았어.... 그것도 욕이야....')  # Bot 종료
        break