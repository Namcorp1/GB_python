import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
    sent = bot.send_message(message.chat.id,'Добрый день! \nКак Вас зовут?')
    bot.register_next_step_handler(sent, hello)
def hello(message):
    bot.send_message(message.chat.id, f'Рад тебя видеть, {message.text}!\nЧтобы узнать список доступных команд, нажми:\n/help (список команд);')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Список доступных команд:\n/start (приветствие);\n/help (список доступных команд);\n/run_calc (беговой калькулятор);')

@bot.message_handler(commands=['run_calc'])
def change_command(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    btn1 = types.KeyboardButton(text='Конвертер скорости и темпа')
    btn2 = types.KeyboardButton(text='Калькулятор темпа')
    kb.add(btn1,btn2)
    bot.send_message(message.chat.id, 'Добро пожаловать в <b>беговой калькулятор</b>!\nВыбери, что хочешь сделать:',parse_mode = 'HTML',reply_markup=kb)

@bot.message_handler(func= lambda x: x.text == 'Калькулятор темпа')
def input_time(message):
    sent = bot.send_message(message.chat.id,"Введите необходимое время в формате 'ЧЧ:ММ:СС': ")
    bot.register_next_step_handler(sent,input_dist)
def input_dist(message):
    sec_arr = message.text.split(':')
    seconds = int(sec_arr[0]) * 3600 + int(sec_arr[1])*60 + int(sec_arr[2])
    sent = bot.send_message(message.chat.id, 'Введите дистанцию в километрах: ')
    bot.register_next_step_handler(sent,calc_pace,seconds)
def calc_pace(message,seconds): #передача 2 аргументов возможно через предыдущую функцию (34 строка)
    if ',' in message.text:
        message.text = message.text.replace(',','.')
    dist = float(message.text)
    pace_min = int(seconds / dist / 60)
    pace_sec = int(seconds / dist - pace_min * 60)
    if pace_sec < 10:
        bot.send_message(message.chat.id,f'Необходимый темп {pace_min}:0{pace_sec} мин/км.')
    else:
        bot.send_message(message.chat.id, f'Необходимый темп {pace_min}:{pace_sec} мин/км.')
@bot.message_handler(func= lambda x: x.text == 'Конвертер скорости')
def choice_converter(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    btn1 = types.KeyboardButton(text='км/ч -> мин/км')
    btn2 = types.KeyboardButton(text='мин/км -> км/ч')
    kb.add(btn1,btn2)
    bot.send_message(message.chat.id,'Что именно хотите конвертировать: ',reply_markup=kb)

@bot.message_handler(func= lambda x: x.text == 'км/ч -> мин/км')
def input_speed(message):
    sent = bot.send_message(message.chat.id,'Введите скорость в км/ч: ')
    bot.register_next_step_handler(sent,speed_to_pace)
def speed_to_pace(message):
    if ',' in message.text:
        message.text = message.text.replace(',','.')
    speed = float(message.text)
    pace_m = int(60 / speed)
    pace_s = int((60 / speed - int(60 / speed)) * 60)
    bot.send_message(message.chat.id,f'{speed} км/ч -> {pace_m}:{pace_s} мин/км')

@bot.message_handler(func= lambda x: x.text == 'мин/км -> км/ч')
def input_pace(message):
    sent = bot.send_message(message.chat.id,"Введите темп в формате 'ММ:СС': ")
    bot.register_next_step_handler(sent, pace_to_speed)
def pace_to_speed(message):
    pace = message.text.split(':')
    time_sec = int(int(pace[0]) * 60 + int(pace[1]))
    speed = float(round(3600 / time_sec,1))
    bot.send_message(message.chat.id,f'{pace[0]}:{pace[1]} мин/км -> {speed} км/ч')

bot.polling()