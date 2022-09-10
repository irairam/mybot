import logging
import settings
# import sys
import os
import signal
from telegram.ext import Updater,  CommandHandler, MessageHandler, Filters

#Включаем логгирование
logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

def greet_user(update, context):
    user = update.message.from_user
    print('You talk with user {} '.format(user['username']))
    update.message.reply_text('Привет, {} '.format(user['username']))

def talk_to_me(update, context):
    user_text = update.message.text
    # пробуем застопать бота на определенное сообщение. 
    # Непонятно как правильно шатдаун сделать
    # и я не первая. Пробуем решение из https://github.com/python-telegram-bot/python-telegram-bot/issues/801
    # todo: добавить проверку на username 
    # почему-то не заработало сходу. Добавила в settings имя админа и проверку на него, но idle висит
    # а цикл проверки ломается и не работает
    if  user_text == 'Остановись':
        update.message.reply_text('Так точно, капитан, работа остановлена')
        os.kill(os.getpid(), signal.SIGINT)
        # sys.exit() #и этот тоже в консоли висит
        # exit() #В консоли все равно висит
        # raise SystemExit(0) #в консоли тоже висит
    else: 
        print(user_text)
        update.message.reply_text(user_text)

if __name__ == '__main__':
    main()