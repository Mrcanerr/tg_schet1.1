from aiogram import Bot, Dispatcher, executor, types
from handlers.start import cmd_start, file_help
from handlers.file_handler import handle_file

TOKEN = "8464230833:AAHuVdH301Oh2vNEplUpYPHlWLYtlQEBZzk"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(cmd_start, commands=["start"])
dp.register_message_handler(file_help, lambda m: m.text == " Как должен выглядеть файл")
dp.register_message_handler(handle_file, content_types=types.ContentType.DOCUMENT)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
