from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Добрый день! \nКак Вас зовут?')

@dp.message_handler()
async def answer_bot(message: types.Message):
    await message.answer(message.text)
