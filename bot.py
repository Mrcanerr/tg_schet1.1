from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from parser import parse_inventory

TOKEN = "8464230833:AAHuVdH301Oh2vNEplUpYPHlWLYtlQEBZzk"


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add("Загрузить файл", "Получить отчет")
kb.add("Как должен выглядеть файл")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Привет. Я бот учета.\nВыбери действие",
        reply_markup=kb
    )

@dp.message_handler(lambda message: message.text == "Загрузить файл")
async def load_file(message: types.Message):
    await message.answer(
        "Пришли Excel файл.\n\n"
        "Формат:\n"
        "Колонка A — товар\n"
        "Колонка B — количество"
    )

@dp.message_handler(content_types=['document'])
async def handle_file(message: types.Message):
    if not message.document.file_name.endswith(".xlsx"):
        await message.answer("Нужен файл .xlsx")
        return

    file = await bot.get_file(message.document.file_id)
    await bot.download_file(file.file_path, "table1.xlsx")

    await message.answer("Файл получен и сохранен")

if __name__ == "__main__":
    executor.start_polling(dp)

