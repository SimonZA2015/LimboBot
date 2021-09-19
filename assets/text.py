import re

import pymysql
from telebot import types

import assets.photo
from assets import tokens
from assets.keysValues import buttonsKey
from assets.tools import tools


class text():
    def __init__(self, bot):
        self.lisener(bot)
        self.user = False
        self.ipv = False
        self.userID = False

    def lisener(self, bot):
        try:
            @bot.message_handler(content_types=['text'])
            def send_text(message):

                if message.text == '🐎 Об мне':
                    tools.setValue(message.chat.id, 'step', 'kedro')
                    bot.send_message(message.chat.id, 'Я Лимбо! Люблю очень поесть, пофыркать на проходящих лошадей с '
                                                      'Кедро, '
                                                      'а так же конюха удивить утром)',
                                     reply_markup=buttonsKey.Kedro(message.chat.id))

                elif message.text == '🛖 Конюшни':
                    if tools.setValue(message.chat.id, "step", "kon1"):
                        bot.send_message(message.chat.id, 'А какой город?', )
                    else:
                        bot.send_message(message.chat.id, 'Эм.. Что-то не так', )
                        tools.setValue(message.chat.id, 'step', False)


                elif message.text == '🛍️ Амуничник':
                    tools.getInfo(bot, message.chat.id, 0)
                    tools.setValue(message.chat.id, 'step', False)

                elif message.text == '👈 Назад':
                    if tools.getValue(message.chat.id, 'step') == 'addIp':
                        bot.send_message(message.chat.id, "Ага", reply_markup=buttonsKey.lognView(message.chat.id))
                        tools.setValue(message.chat.id, 'step', "login")

                    else:
                        bot.send_message(message.chat.id, "Ага", reply_markup=buttonsKey.homeView(message.chat.id))
                        tools.setValue(message.chat.id, 'step', False)

                elif message.text == '💬 Помощь':
                    bot.send_message(message.chat.id,
                                     'Я могу тебе подсказать кон, показать из амуничника интересные вещи)',
                                     reply_markup=buttonsKey.homeView(message.chat.id))
                    tools.setValue(message.chat.id, 'step', False)

                elif message.text == 'Частник':
                    tools.setValue(message.chat.id, 'step', 'admin1')
                    bot.send_message(message.chat.id, 'Как вы хотите админу написать?',
                                     reply_markup=buttonsKey.adminView(message.chat.id))

                elif message.text == 'Сообщить всем>':
                    if (message.chat.id == tokens.userAdminChat):
                        tools.setValue(message.chat.id, 'step', 'sendAll1')
                        bot.send_message(message.chat.id, 'Что сообщить?')

                    else:
                        bot.send_message(message.chat.id, 'Говори по лошидиному! Я не понимаю тебя')
                        tools.setValue(message.chat.id, 'step', False)

                elif message.text == "Добавить>":
                    if message.chat.id == tokens.userAdminChat:
                        tools.setValue(message.chat.id, 'step', 'addInfo1')
                        bot.send_message(message.chat.id, 'Что добавить?',
                                         reply_markup=buttonsKey.addView(message.chat.id))

                    else:
                        bot.send_message(message.chat.id, 'Говори по лошидиному! Я не понимаю тебя')
                        tools.setValue(message.chat.id, 'step', False)

                else:
                    result = tools.getValue(message.chat.id, "step")
                    if (result == False):
                        bot.send_message(message.chat.id, 'Говори по лошидиному! Я не понимаю тебя')

                    elif (result == "kon1"):
                        bot.send_message(message.chat.id, "Ищу кон")
                        tools.setValue(message.chat.id, 'step', False)

                    elif (result == 'kedro'):
                        tools.setValue(message.chat.id, 'step', False)
                        if message.text == 'Кедро?':
                            bot.send_message(message.chat.id,
                                             'Кедро мой друг! Он живет по соседству с ним. Бываем балуемся, хихикаем, гуляем в леваде обсуждая кобыл в соседней леваде)',
                                             reply_markup=buttonsKey.homeView(message.chat.id))
                    elif (result == 'addInfo1'):
                        if message.text == 'Амуничник':
                            tools.setValue(message.chat.id, 'step', 'addInfo_A')
                            bot.send_message(message.chat.id,
                                             'Добавле фотаграфию с текстом',
                                             reply_markup=buttonsKey.BackView(message.chat.id))
                        elif message.text == 'Конюшня':
                            tools.setValue(message.chat.id, 'step', 'addInfo_S')
                            bot.send_message(message.chat.id,
                                             'Добавле фотаграфию с текстом',
                                             reply_markup=buttonsKey.BackView(message.chat.id))
                        elif message.text == 'Новость':
                            tools.setValue(message.chat.id, 'step', 'addInfo_N')
                            bot.send_message(message.chat.id,
                                             'Добавле фотаграфию с текстом',
                                             reply_markup=buttonsKey.BackView(message.chat.id))
                        elif message.text == '👈 Назад':
                            tools.setValue(message.chat.id, 'step', False)
                            bot.send_message(message.chat.id,
                                             'Ага',
                                             reply_markup=buttonsKey.homeView(message.chat.id))
                        else:
                            bot.send_message(message.chat.id,
                                             'Попоробуй выбрать из кнопок')

                    elif result == 'admin1':
                        if message.text == 'Через тебя':
                            tools.setValue(message.chat.id, 'step', 'admin2')
                            bot.send_message(message.chat.id, 'Что сообщить?',
                                             reply_markup=buttonsKey.BackView(message.chat.id))
                        elif message.text == 'ВК':
                            bot.send_message(message.chat.id, 'Вот его вк: https://vk.com/denis_hik',
                                             reply_markup=buttonsKey.homeView(message.chat.id))
                            tools.setValue(message.chat.id, 'step', False)
                        elif message.text == 'Инста':
                            bot.send_message(message.chat.id, 'Вот его инста: https://instagram.com/denis_hik',
                                             reply_markup=buttonsKey.homeView(message.chat.id))
                            tools.setValue(message.chat.id, 'step', False)
                        else:
                            bot.send_message(message.chat.id, 'Выбери из кнопок')
                            tools.setValue(message.chat.id, 'step', 'admin1')

                    elif result == 'admin2':
                        bot.send_message(tokens.userAdminChat,
                                         str(message.chat.id) + '(' + message.chat.username + ")> " + message.text)
                        bot.send_message(message.chat.id, 'Я ему передам)')
                        tools.setValue(message.chat.id, 'step', False)



                    elif (result == 'sendAll1'):
                        tools.setValue(message.chat.id, 'step', False)
                        if (message.chat.id == tokens.userAdminChat):
                            tools.sendAll(bot, message.text)
                        else:
                            bot.send_message(message.chat.id, 'Ошибка! Ты не мой хозяин!',
                                             reply_markup=buttonsKey.homeView(message.chat.id))

                    elif (result == 'login'):
                        data = [False, False]
                        try:
                            #get message text
                            data = message.text

                            #get login & password
                            data = data.split(' ', 1)

                            #get login base
                            dbNAme = tokens.dbBase

                            userDb = data[0].split('@', 1)[0]
                            if (data[0] and data[1]):
                                command = "SELECT `users`.* FROM `users`;"
                                print(command + data[0] + data[1])
                                usersDB = tools.loginBase(command, data[0], data[1])

                                for user in usersDB:
                                    if (user[1] == data[0]):
                                        self.userID = user[0]
                                        self.ipsBase = user[3]

                                self.userDb = userDb
                                self.user = data[0]
                                self.password = data[1]
                                bot.send_message(message.chat.id, 'Привет,' + str(data[0]),
                                                 reply_markup=buttonsKey.lognView(message.chat.id))
                                tools.setValue(message.chat.id, 'step', 'login1')

                        except Exception as e:
                            bot.send_message(message.chat.id, 'Чтото не так\n' + str(e), reply_markup=buttonsKey.errorInline(message.chat.id))

                            pass

                    elif (result == 'login1'):
                        if (message.text == 'Clear ips'):
                            tools.clear_ips(self.user, self.password, self.userID)
                            bot.send_message(message.chat.id, 'IP list очищен',
                                             reply_markup=buttonsKey.lognView(message.chat.id))
                            self.ipsBase = ''
                            tools.setValue(message.chat.id, 'step', 'login1')

                        if (message.text == 'Sign Out'):
                            bot.send_message(message.chat.id, 'Успешный выход',
                                             reply_markup=buttonsKey.homeView(message.chat.id))
                            tools.setValue(message.chat.id, 'step', False)

                        if (message.text == 'Add ip'):
                            bot.send_message(message.chat.id, 'Напишите Ipv6 ваш', reply_markup=buttonsKey.addIpView(message.chat.id))
                            tools.setValue(message.chat.id, 'step', 'addIp')

                    elif (result == 'addIp'):
                        ipInput = message.text
                        if (message.text == 'Your ipv6'):
                            ipInput = tools.get_ip(message.text)

                        if (self.userID == False):
                            bot.send_message(message.chat.id, 'UserId not found',
                                             reply_markup=buttonsKey.lognView(message.chat.id))
                            tools.setValue(message.chat.id, 'step', 'login1')

                        else:
                            try:
                                self.ipsBase.index(ipInput)
                                bot.send_message(message.chat.id, 'IP уже есть',
                                                 reply_markup=buttonsKey.lognView(message.chat.id))
                                tools.setValue(message.chat.id, 'step', 'login1')

                            except:
                                tools.updateIpBase(self.user, self.password, self.ipsBase + ',' + ipInput, self.userID)
                                bot.send_message(message.chat.id, 'IP добавлен',
                                                 reply_markup=buttonsKey.lognView(message.chat.id))
                                tools.setValue(message.chat.id, 'step', 'login1')



                    elif (result == 'close'):
                        if (message.chat.id == tokens.userAdminChat):
                            tools.setValue(message.chat.id, 'step', False)
                            print('Bot stopping...')
                            print('s' + 1)

                        else:
                            bot.send_message(message.chat.id, 'Ошибка! Ты не мой хозяин!',
                                             reply_markup=buttonsKey.homeView(message.chat.id))
                            tools.setValue(message.chat.id, 'step', False)
                    else:
                        bot.send_message(message.chat.id, 'Говори по лошидиному! Я не понимаю тебя')
                        tools.setValue(message.chat.id, 'step', False)

        except Exception as e:
            print('BOT> Error in text.py{lisener}: ', e)
