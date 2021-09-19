import telebot

from assets import tokens
from assets.commands import commands
from assets.photo import photo
from assets.text import text
def close():
    s = 0
    print('a' + s)
bot = telebot.TeleBot(tokens.tokenTelegram)
try:
    error = False
    commands(bot, close, error)
    text(bot, error)
    photo(bot, error)

except Exception as e:
    print('BOT> Произошла ошибка: ', e)



print('started')
bot.polling(none_stop=True)
