from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

api = "xxxxxxxxxx:xxxxxxxxxxxxxxxxxxxxx"
bot = Bot(token = api)
storage = MemoryStorage()  # для наглядности создаётся явно
dp = Dispatcher(storage = MemoryStorage())

@dp.message.register
async def handle_text_message(message):
    # Удаляем лишние пробелы и приводим текст к нижнему регистру
    user_text = message.text.strip().lower()
    # Проверяем, соответствует ли текст "привет!" (с восклицательным знаком)
    if user_text == '/start':
        # await message.reply('Хай')
        print("Привет! Я бот помогающий твоему здоровью.")
    if user_text == 'хай':
        # await message.reply('Привет')
        print("Мы получиои сообщение Привет")

    print("Введите команду /start, чтобы начать общение.")
    # await message.reply('Я Грут')
    # print(f"Мы получиои сообщение {user_text}")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    if __name__ == '__main__':
        asyncio.run(main())

