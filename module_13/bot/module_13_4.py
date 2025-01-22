from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
import asyncio

api = "TOKEN"
bot = Bot(token=api)
# storage = MemoryStorage()  # для наглядности создаётся явно
dp = Dispatcher()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message(lambda message: message.text == 'Calories')
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.age)
    await message.answer('Введите свой возраст:',
reply_markup=ReplyKeyboardRemove(),)

@dp.message(UserState.age)
async def process_age(message: Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    await state.set_state(UserState.growth)
    await message.answer('Введите свой рост:',
                         reply_markup=ReplyKeyboardRemove(), )
@dp.message(UserState.growth)
async def process_growth(message: Message, state: FSMContext) -> None:
    await state.update_data(growth=message.text)
    await state.set_state(UserState.weight)
    await message.answer('Введите свой вес:',
                         reply_markup=ReplyKeyboardRemove(), )

@dp.message(UserState.weight)
async def process_weight(message: Message, state: FSMContext) -> None:
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data.get('age', 0))
    growth = int(data.get('growth', 0))
    weight = int(data.get('weight', 0))

    # Формула для расчета нормы калорий (например, для мужчин)
    # BMR = 10 * weight + 6.25 * height - 5 * age + 5
    # Вам необходимо изменить формулу в зависимости от пола или других критериев
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша норма калорий: {bmr} ккал.")

    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

age = 18
growth = 190
weight = 86