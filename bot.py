import logging
import settings
import sys
from telegram.ext import Updater,  CommandHandler, MessageHandler, Filters

#Включаем логгирование
logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text
    if user_text == 'Остановись':
        update.message.reply_text('Так точно, капитан, работа остановлена')
        exit() #Почему в шелле не останавливает? (
        # raise SystemExit(0) #какого черта не работает?
    else: 
        print(user_text)
        update.message.reply_text(user_text)

# Вызываем функцию main(). Неправильный вариант: 
# main()

#А вот так правильно:
if __name__ == '__main__':
    main()