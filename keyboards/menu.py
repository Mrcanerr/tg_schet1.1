from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = KeyboardButton(" Загрузить файл")
btn2 = KeyboardButton(" Получить отчет")
btn3 = KeyboardButton(" Как должен выглядеть файл уёбище")

main_menu.add(btn1, btn2)
main_menu.add(btn3)
