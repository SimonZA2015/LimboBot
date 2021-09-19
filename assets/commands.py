from telebot import types

from assets import tokens
from assets.keysValues import buttonsKey
from assets.tools import tools


class commands():
    def __init__(self, bot, close):
        self.lisener(bot)
        self.close = close

    def lisener(self, bot):
        @bot.message_handler(commands=['start'])
        def start_message(message):
            tools.saveId(message.chat.id, message.chat.username)
            bot.send_message(message.chat.id, 'Привет, я Лимбо! Готов тебе помочь в изучении конного спорта!',
                             reply_markup=buttonsKey.homeView(message.chat.id))

        @bot.message_handler(commands=['close'])
        def close_message(message):
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            btn3 = types.KeyboardButton('👈 Назад')
            btn4 = types.KeyboardButton('Да')
            tools.setValue(message.chat.id, 'step', "close")
            markup.add(btn3, btn4)
            print('BOT> request stop. idUser:', message.chat.id , "Name: ", message.from_user.id)
            bot.send_message(message.chat.id, 'Дествительно ли выключить бота?',
                             reply_markup=markup)


        @bot.message_handler(commands=['login'])
        def login_messagee(message):
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            btn3 = types.KeyboardButton('👈 Назад')
            tools.setValue(message.chat.id, 'step', 'login')
            markup.add(btn3)
            bot.send_message(message.chat.id, 'Ого! Ты хочешь войти в админ панель? Веди через пробел логин м пароль',
                             reply_markup=markup)
