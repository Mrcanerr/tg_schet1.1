from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = KeyboardButton("Загрузить файл")
btn2 = KeyboardButton("Получить отчет")
btn3 = KeyboardButton("Как должен выглядеть файл")

main_kb.add(btn1, btn2, btn3)
