from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove, InputFile

from filters import IsGroup
from loader import dp, bot


@dp.message_handler(IsGroup(), Text("show_on_map"))
async def share_number(message: types.Message):
    URL = "http://maps.google.com/maps?q=45.001409,41.129644"

    photo_bytes = InputFile(path_or_bytesio="items/photo/location.png")
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_bytes,
                         caption=f"Мы находимся здесь \n"
                         f"<a href='{URL}'>Краснодарский край, г. Армавир, улица Карла Либнехта 48, офис 43</>")

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"{message.from_user.first_name} теперь у тебя есть наши координаты\n"
                           f"Если хочешь узнать больше о нас, то в левой менюшке можешь выбрать команду /about \n"
                           f"либо просто нажать на эту команду здесь")