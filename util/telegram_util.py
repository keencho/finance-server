import telegram


def  telegram_send(token: str, chat_id: str, text: str):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id, text=text)