# -*- coding: utf-8 -*-import telebot

## СНАЧАЛА УСТАНОВИТЕ БИБЛИОТЕКУ
# pip3 install pytelegrambotapi
# или pip install pytelegrambotapi


from telebot import types

bot = telebot.TeleBot('BOT-TOKEN')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Математика")
    btn2 = types.KeyboardButton("Физика")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник! Какую домашку тебе скинуть ?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    file = open(message.text, 'rb')
    bot.send_document(message.chat.id, file)





bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть