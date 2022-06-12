from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
location_button = KeyboardButton("/share location")
start_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
