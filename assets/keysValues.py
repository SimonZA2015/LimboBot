from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from assets import tokens


class buttonsKey():
    def adminView(idTelegram):
        markupHome = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        merop = types.KeyboardButton('Через тебя')
        info = types.KeyboardButton('ВК')
        btn3 = types.KeyboardButton('Инста')
        markupHome.add(merop, info, btn3)
        return markupHome

    def addView(self):
        markupHome = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        merop = types.KeyboardButton('Амуничник')
        info = types.KeyboardButton("Конюшня")
        btn3 = types.KeyboardButton('Новость')
        back = types.KeyboardButton('👈 Назад')
        markupHome.add(merop, info, btn3, back)
        return markupHome

    def homeView(idTelegram):
        markupHome = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        merop = types.KeyboardButton('🛖 Конюшни')
        info = types.KeyboardButton('🐎 Об мне')
        btn3 = types.KeyboardButton('💬 Помощь')
        btn4 = types.KeyboardButton('🛍️ Амуничник')
        athor = types.KeyboardButton('Частник')
        if (idTelegram == tokens.userAdminChat):
            sendAll = types.KeyboardButton('Сообщить всем>')
            addTovars = types.KeyboardButton('Добавить>')
            close = types.KeyboardButton(text='/close')
            markupHome.add(merop, info, btn3, btn4, sendAll, close, addTovars)
        else:
            markupHome.add(merop, info, btn3, btn4, athor)
        return markupHome

    def Kedro(self):
        markupKedro = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
        btn5 = types.KeyboardButton('👈 Назад')
        btn6 = types.KeyboardButton('Кедро?')
        markupKedro.add(btn5, btn6)
        return markupKedro

    def BackView(self):
        markupBack = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn7 = types.KeyboardButton('👈 Назад')
        markupBack.add(btn7)
        return markupBack

    def errorInline(self):
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="More", callback_data="error_more")
        key.add(but_1)
        return key
