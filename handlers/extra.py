from aiogram import types, Dispatcher
from config import dp, bot, ADMIN
import random


async def echo_1(message: types.Message):
    a = int(message.text)
    await bot.send_message(message.from_user.id, a ** 2)

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_1)
