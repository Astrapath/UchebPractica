import random
from datetime import datetime

import json
import requests
import telebot
import weather_data
from telebot import types


def birthdaycounter(message):
    today = datetime.now()
    thisyear = today.year
    birthdaydate = datetime(thisyear, 5, 26)
    delta = (birthdaydate - today).days
    if delta == 0:
        bot.reply_to(message, 'HAPPY BIRTHDAY MY CREATOR!')
    else:
        bot.reply_to(message, f'The birthday of my creator will be through {delta} days ')


def get_cat_image_url():
    responce = requests.get('https://api.thecatapi.com/v1/images/search').text
    return json.loads(responce)[0]['url']


def ultrakill():
    images = ['https://i.pinimg.com/originals/90/92/86/909286d9f618a8130c152bce0f5f9741.jpg',
              'https://i.pinimg.com/originals/79/92/02/7992022390bd70e0ffed31273d17438d.jpg',
              'https://i.pinimg.com/736x/68/77/e5/6877e5d73231a0aec96db33d593bcb05.jpg',
              'https://i.pinimg.com/736x/63/a4/f8/63a4f805f2f5ce1521d7d2538c208f26.jpg',
              'https://i.pinimg.com/736x/37/08/19/370819804a7c1c4d412a5c72a3371cc1.jpg',
              'https://i.pinimg.com/736x/11/91/9b/11919bb04a163dcc345319f4d803c114.jpg',
              'https://i.pinimg.com/736x/e4/7c/bb/e47cbb7eb96fad235144a384aa45012f.jpg',
              'https://i.pinimg.com/736x/62/2d/f1/622df15a4618fe94f4a784fd11197466.jpg',
              'https://i.pinimg.com/736x/54/45/d0/5445d0a214e63bfa25ea0e5ef648bd91.jpg']
    return random.choice(images)


def goida():
    gifs = ['https://c.tenor.com/2DvsxhuUB9QAAAAC/tenor.gif',
            'https://media1.tenor.com/m/DlQRhYXcg1wAAAAd/гойда-мегагойда.gif',
            'https://c.tenor.com/AH8ePKM3Zm4AAAAd/tenor.gif',
            'https://c.tenor.com/dg6KwQSCPPwAAAAd/tenor.gif',
            'https://media1.tenor.com/m/SFi-TnmCdyAAAAAd/гойда-радость.gif',
            'https://media1.tenor.com/m/UC8TDXxucKgAAAAd/goida-гойда.gif'
            ]
    return random.choice(gifs)


def i_drive():
    drive = ['https://c.tenor.com/B8xT8mGbzz0AAAAd/tenor.gif']
    return drive[0]


token = '7625725163:AAE0xyIiEZzEl1Pzy8qt7cFDWnQY5fjYJGk'
bot = telebot.TeleBot(token)
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
btn_cat = types.KeyboardButton('i need cat')
btn_drive = types.KeyboardButton('i drive')
btn_ultrakill = types.KeyboardButton('IS THAT ULTRAKILL?')
btn_goida = types.KeyboardButton('GOIDA')
btn_weather = types.KeyboardButton('i need to know weather at city')
btn_birthday = types.KeyboardButton('when is your creator birthday?')
keyboard.add(btn_cat, btn_drive, btn_weather, btn_birthday, btn_goida, btn_ultrakill)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "hey, how are you doing?", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def answer(message):
    if message.text == 'i need cat':
        image_url = get_cat_image_url()
        bot.send_photo(message.chat.id, image_url)
    elif message.text == 'IS THAT ULTRAKILL?':
        image = ultrakill()
        bot.send_photo(message.chat.id, image)
    elif message.text == 'GOIDA':
        gif_url = goida()
        bot.send_video(message.chat.id, gif_url, None, 'Text')
    elif message.text == 'i drive':
        gif_url = i_drive()
        bot.send_video(message.chat.id, gif_url, None, 'Text')
    elif message.text not in ['i need cat', 'i need dog', 'i drive', 'i drive', 'i need to know weather at city',
                              'when is your creator birthday?']:
        bot.send_message(message.chat.id, "Can you use buttons? im lazy to create some answers for random words")
    elif message.text == 'i need to know weather at city':
        bot.send_message(message.chat.id, "alright, for what city you need it?")
        bot.register_next_step_handler(message, send_weather)
    elif message.text == 'when is your creator birthday?':
        birthdaycounter(message)


def send_weather(message):
    bot.send_message(message.chat.id, weather_data.get_weather_data(message.text))


bot.infinity_polling()
