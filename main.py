import telebot
from telebot import types
import random
import codecs
import os
import schedule
import time


bot = telebot.TeleBot("your token")
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    pic = open('stic/N9128ZN5_s0.jpg', 'rb')
    always()
    bot.reply_to(message, "Привет! \nЭтот маленький подарочек для тебя)".format(message.from_user),
                 reply_markup=markup)
    bot.send_sticker(message.chat.id, pic)


def always():
    but1 = types.KeyboardButton("Котики")
    but3 = types.KeyboardButton("Анекдот")
    markup.add(but1, but3)


def anegdot(message):
    b = random.randint(0, 18)
    bot.send_message(message.chat.id, codecs.open("anegdot/all.txt", "r", "utf-8").read().split('<|startoftext|>')[b])


def kitty(message):
    bot.send_photo(message.chat.id, open('kitty/' + random.choice(os.listdir('kitty')), 'rb'))


@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.text == 'Котики':
        kitty(message)
    if message.text == 'Анекдот':
        anegdot(message)



def gn(message):
    bot.send_message(message.chat.id, "Доброй ночи!)".format(message.from_user), reply_markup=markup)


def gm(message):
    bot.send_message(message.chat.id, "Доброй ночи!)".format(message.from_user), reply_markup=markup)


schedule.every().day.at("23:00").do(gn)
schedule.every().day.at("07:00").do(gm)


while True:
    schedule.run_pending()
    time.sleep(1)
    bot.polling(none_stop=True)