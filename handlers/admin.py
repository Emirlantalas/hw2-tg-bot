from aiogram import types, Dispatcher
from config import bot, ADMIN
import random



async def echo(message: types.Message):
    bad_words = ['дурак', "плохой", 'java', 'js', 'uxui']
    for word in bad_words:
        if word in message.text.lower():
            await bot.send_message(message.chat.id,
                                   f"Не матерись {message.from_user.full_name} "
                                   f"сам ты {word}")
            await bot.delete_message(message.chat.id, message.message_id)

    if message.text.startswith('pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text.lower() == 'dice':
        d = await bot.send_dice(message.chat.id, emoji='🎯')
        print(d.dice.value)


async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id != ADMIN:
            await message.answer("Ты не мой БОСС!!!")
        elif not message.reply_to_message:
            await message.answer("Комманда должна быть ответом на сообщение!")
        else:
            await message.bot.kick_chat_member(message.chat.id,
                                               user_id=message.reply_to_message.from_user.id)
            await message.answer(f"Пользователь {message.reply_to_message.from_user.full_name} "
                                 f"был забанен по воле {message.from_user.full_name}")

    else:
        await message.answer("Это работает только в группах")


async def pin(message: types.Message):
    if message.from_user.id != ADMIN:
        await message.reply("Ты не мой admin!")
    if not message.reply_to_message:
        await message.reply("Команда должна быть ответом на сообщение!")
    else:
        if message.text.startswith("!pin"):
            await bot.pin_chat_message(message.chat.id, message.message_id)


# async def echo2(message: types.Message):
#     if message.text.startswith('pin'):
#         await bot.pin_chat_message(message.chat.id, message.message_id)
#     await bot.send_message(message.from_user.id, message.text)
#     # a = int(message.text)
#     # await bot.send_message(message.from_user.id, a ** 2)





def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix="!/")
    dp.register_message_handler(pin, commands=["pin"], commands_prefix="!")
