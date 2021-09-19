class error():
    def __init__(self, bot):
        self.error = False
        self.init(bot)

    def init(self, bot):
        @bot.callback_query_handler(func=lambda c: True)
        def inlin(c):
            if c.data == 'error_more':
                bot.send_message(c.message.chat.id, self.error)