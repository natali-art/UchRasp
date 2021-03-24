import telebot
bot = telebot.TeleBot('1723704255:AAEMH1m1C5r2WNrKfGkHpLUN_78lu3Yg_xs')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот-расписание и помогу тебе не опоздать на урок. Приятно познакомиться, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        if message.text.lower() == 'Как дела?':
            bot.send_message(message.from_user.id, 'Отлично!')
        else:
            bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

bot.polling(none_stop=True)
