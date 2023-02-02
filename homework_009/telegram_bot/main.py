import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
    sent = bot.send_message(message.chat.id,'Добрый день! \nКак Вас зовут?')
    bot.register_next_step_handler(sent, hello)
def hello(message):
    bot.send_message(message.chat.id, f'Рад тебя видеть, {message.text}!\nВот список доступных команд:\n/start (приветствие);\n/help (список команд);')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Список доступных команд:\n/start (приветствие);\n/help (список доступных команд);')

bot.polling()