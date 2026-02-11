from aiogram import types
from keyboards.menu import main_menu

async def cmd_start(message: types.Message):
    await message.answer(
        "Привет. Я бот учета.\nВыбери действие Уёбок:",
        reply_markup=main_menu
    )

async def file_help(message: types.Message):
    text = (
        "Файл должен быть Excel (.xlsx)\n\n"
        "Колонка A — название товара\n"
        "Колонка B — количество\n\n"
        "Без пустых строк в середине."
    )

    await message.answer(text)
