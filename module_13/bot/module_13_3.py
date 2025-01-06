from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

api = "xxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
bot = Bot(token = api)
storage = MemoryStorage()  # для наглядности создаётся явно
dp = Dispatcher(storage = MemoryStorage())

@dp.message.register
async def handle_text_message(message):
    # Удаляем лишние пробелы и приводим текст к нижнему регистру
    user_text = message.text.strip().lower()
    # Проверяем, соответствует ли текст "привет!" (с восклицательным знаком)
    if user_text == '/start':
        await message.reply('Привет! Я бот помогающий твоему здоровью.')
        # print("Привет! Я бот помогающий твоему здоровью.")
    else:
        # print("Введите команду /start, чтобы начать общение.")
        await message.reply("Введите команду /start, чтобы начать общение.")
        # print(f"Мы получиои сообщение {user_text}")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    if __name__ == '__main__':
        asyncio.run(main())

