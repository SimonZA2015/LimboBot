import telebot

from assets import tokens
from assets.commands import commands
from assets.text import text
def close():
    s = 0
    print('a' + s)
bot = telebot.TeleBot(tokens.tokenTelegram)
try:
    commands(bot, close)
    text(bot)

except Exception as e:
    print('BOT> Произошла ошибка: ', e)



print('started')
bot.polling(none_stop=True)