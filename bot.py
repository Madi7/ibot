# Third-Party
from telegram.ext import (
    Updater,
    CommandHandler, MessageHandler,
    Filters
)


updater = Updater(
    token='555331704:AAFK_grKeGaMCEgY_MqVizteFXSwA9dqcys'
)
dispatcher = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Привет, давай пообщаемся?'
    )


def textMessage(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response
    )


start_command_handler = CommandHandler(
    'start',
    startCommand
)
text_message_handler = MessageHandler(
    Filters.text,
    textMessage
)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

# Stop Bot on -> [ctrl+c]
updater.idle()
