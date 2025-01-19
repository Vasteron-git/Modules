from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

api = "TOKEN"
bot = Bot(token=api)
# storage = MemoryStorage()  # для наглядности создаётся явно
dp = Dispatcher()

# Функция для обработки команды /start
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

# Функция для обработки всех остальных сообщений
@dp.message(F.text)
async def all_messages(message: Message):
    await message.answer(f"Введите команду /start, чтобы начать общение.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

