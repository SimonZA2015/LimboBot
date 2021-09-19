from assets.keysValues import buttonsKey
from assets.tools import tools


class photo():
    def __init__(self, bot):
        self.error = False
        self.lisener(bot)

    def lisener(self, bot):
        try:
            @bot.message_handler(content_types=['photo'])
            def photo_message(message):
                try:
                    status = tools.getValue(message.chat.id, 'step')
                    if status == 'addInfo_A':
                        if len(message.caption) > 0:
                            # bot.send_photo(message.chat.id, message.photo[0].file_id, caption=message.caption)
                            type = 0
                            text1 = 'Смотри! Амуня!\n'
                            tools.addInfo(type, message.photo[0].file_id, message.caption)
                            tools.sendPhotoAll(bot, message.photo[0].file_id, text1 + message.caption)
                            tools.setValue(message.chat.id, 'step', False)

                        else:
                            tools.setValue(message.chat.id, 'step', 'addInfo_Acaption')
                            bot.send_message(message.chat.id, 'Добавте текст')

                    if status == 'addInfo_S':
                        if len(message.caption) > 0:
                            # bot.send_photo(message.chat.id, message.photo[0].file_id, caption=message.caption)
                            type = 1
                            text1 = 'Cмотри! Конюшня!'
                            tools.addInfo(type, message.photo[0].file_id, message.caption)
                            tools.sendPhotoAll(bot, message.photo[0].file_id, text1 + message.caption)
                            tools.setValue(message.chat.id, 'step', False)

                        else:
                            tools.setValue(message.chat.id, 'step', 'addInfo_Acaption')
                            bot.send_message(message.chat.id, 'Добавте текст')


                    if status == 'addInfo_N':
                        if len(message.caption) > 0:
                            # bot.send_photo(message.chat.id, message.photo[0].file_id, caption=message.caption)
                            type = 2
                            text1 = 'Новости!\n'
                            tools.addInfo(type, message.photo[0].file_id, message.caption)
                            tools.sendPhotoAll(bot, message.photo[0].file_id, text1 + message.caption)
                            tools.setValue(message.chat.id, 'step', False)

                        else:
                            tools.setValue(message.chat.id, 'step', 'addInfo_Acaption')
                            bot.send_message(message.chat.id, 'Добавте текст')
                except Exception as e:
                    self.error = e
                    print('BOT> Error in photo.py{photo_message}: ', e)
                    bot.send_message(message.chat.id, 'Ошибка, попробуй снова', reply_markup=buttonsKey.errorInline(message.chat.id))

            @bot.callback_query_handler(func=lambda c: True)
            def inlin(c):
                if c.data == 'error_more':
                    bot.send_message(c.message.chat.id, self.error)


        except Exception as e:
            self.error = e
            print('BOT> Error in phtot.py{lisener}: ', e)

    def setError(self, error):
        self.error = error
