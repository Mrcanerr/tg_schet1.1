from aiogram import types
from keyboards.confirm import confirm_keyboard
from utils.report import create_report

async def handle_file(message: types.Message):

    await message.answer("Файл получен, начинаю обработку...(уёбищеее)")

    # пример данных отчета (пока тест)
    rows = [
        {"name": "Лан", "new": 120, "old": 100, "diff": 20}
    ]

    filename = create_report(rows)

    # отправка файла
    with open(filename, "rb") as f:
        await message.answer_document(f)

    # пример подтверждения
    await message.answer(
        "Все совпадения корректны?",
        reply_markup=confirm_keyboard()
    )
