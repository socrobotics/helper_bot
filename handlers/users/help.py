from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("⁉️Напишите в техподдержку - @SocroboticHelp_bot",
            "👇 Или воспользоваться списоком команд: ",
            "",
            "/start - Начать работу",
            "/shop_telega - Перейти в телеграм магазин FB аккаунтов",
            "/shop_site - Перейти на сайт в магазин FB аккаунтов",
            "/convert_money - Сконвертировать валюту",
            "/buy_proxy - Купить прокси",
            "/about - Узнать больше о Нас",
            "/show_on_map - Узнать где мы базируемся",
            "/help - Задать вопрос в техподдержку")
    
    await message.answer("\n".join(text),
                         reply_markup=types.ReplyKeyboardRemove())
