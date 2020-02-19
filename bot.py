from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = "Здравствуйте, {}! Вы написали: {}".format(update.message.chat.first_name, update.message.text) 
    logging.info("First name: %s, Last name: %s, Chat id: %s, Message: %s", update.message.chat.first_name,
                 update.message.chat.last_name, update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()

# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# import logging



# REQUEST_KWARGS={
#     'proxy_url': 'socks5://t2.learn.python.ru:1080',
#     # Optional, if you need authentication:
#     'urllib3_proxy_kwargs': {
#         'username': 'learn',
#         'password': 'python',
#     }
# }

# logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', 
#     level=logging.INFO, filename='bot.log')

# TOKEN = "1048678174:AAHUhAltcRkG4hTQ0hGvBqKp1uF1q-2lXHc"

# def connect_to_bot():
#     # Here we establish bot connection
#     my_bot = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)

#     dp = my_bot.dispatcher
#     dp.add_handler(CommandHandler("start", greet_user))
#     dp.add_handler(MessageHandler(Filters.text, talk_to_me))

#     my_bot.start_polling()
#     my_bot.idle()

# def greet_user(bot, update):
#     # Here we react at the user's command
#     text = "Hello, my friend! You called /start"
#     print("Copy: ", text)

#     update.message.reply_text(text)

# def talk_to_me(bot, update):
#     # Here we echo user's input
#     user_text = update.message.text 
#     print(user_text)
#     update.message.reply_text(user_text + "?! Какую ерунду ты несёшь!")

# connect_to_bot()