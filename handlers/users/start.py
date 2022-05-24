from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.markdown import hbold

from keyboards.inline.menu import menu_start
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, <b>{message.from_user.full_name}</>!\n\n"
                         f"Я бот-помощник Socrobotic\n\n"
                         f"Могу ответить на большое количество вопросов ежесекундно и по делу\n\n"
                         f"Если хочешь пообщаться - нажми кнопку <b>Задать вопрос боту помощнику</>\n\n"
                         f"Или выбери другой вариант👇 👇 👇 ",
                         reply_markup=menu_start)
