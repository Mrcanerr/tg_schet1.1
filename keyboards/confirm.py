from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def confirm_keyboard():
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("Да", callback_data="confirm_yes"),
        InlineKeyboardButton("Нет", callback_data="confirm_no")
    )
    return kb
