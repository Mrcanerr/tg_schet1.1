import logging
from aiogram import Bot, Dispatcher, executor, types
from keyboards import main_kb

TOKEN = "8464230833:AAHuVdH301Oh2vNEplUpYPHlWLYtlQEBZzk"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer(
        "Привет. Я бот учета.\nВыбери действие",
        reply_markup=main_kb
    )


@dp.message_handler(lambda message: message.text == "Загрузить файл")
async def upload_handler(message: types.Message):
    await message.answer("Отправьте Excel файл (.xlsx)")


@dp.message_handler(lambda message: message.text == "Получить отчет")
async def report_handler(message: types.Message):
    await message.answer("Отчет пока в разработке")


@dp.message_handler(lambda message: message.text == "Как должен выглядеть файл")
async def help_handler(message: types.Message):
    await message.answer(
        "Файл должен быть Excel (.xlsx)\n\n"
        "Колонка A — Наименование товара\n"
        "Колонка B — Количество"
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

