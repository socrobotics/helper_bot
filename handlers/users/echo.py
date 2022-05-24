from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from handlers.users.get_code import get_code_kopeechka
from keyboards.inline.menu import menu, menu_close, menu_again
from loader import dp

import threading

token = []
email = []


@dp.message_handler(Text(contains="оддержка"))
async def close_app(message: types.Message):
    await message.answer(f"{message.from_user.first_name} Вы можете задать свой вопрос в нашу техподдержку @SocroboticHelp_bot\n\n"
                         f"или любому из саппортов:\n\n"
                         f"<b>По вопросам связанным с аккаунтами:</>\n"
                         f"@eduardnos\n"
                         f"@mamaevmaksi\n"
                         f"@viktoriavergi\n\n"
                         f"<b>По вопросам связанным с софтом:</>\n"
                         f"@pharaon93rus\n"
                         f"@clever_ded\n\n"
                         f"<b>По крайне важным вопросам писать админу:</> - @makarovdenis89",
                         reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(Text(contains="купить аккаунты"))
async def close_app(message: types.Message):
    await message.answer(f"@SocroboticStoreBot - Телеграм-магазин FB аккаунтов\n"
                         f"socrobotic.io - удобный интернет-магазин FB аккаунтов",
                         reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(Text(contains="shop_telega"))
async def close_app(message: types.Message):
    await message.answer(f"@SocroboticStoreBot - Телеграм-магазин FB аккаунтов",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(contains="shop_site"))
async def close_app(message: types.Message):
    await message.answer(f"socrobotic.io - удобный интернет-магазин FB аккаунтов",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(contains="Задать вопрос боту помощнику"))
async def close_app(message: types.Message):
    await message.answer(f"{message.from_user.first_name} - задайте свой вопрос"
                         f"и я постараюсь на него ответить",
                         reply_markup=menu_close)



@dp.message_handler(Text(contains="Пообщаться с тех поддержкой socrobotic"))
async def close_app(message: types.Message):
    await message.answer(f"@SocroboticHelp_bot здесь вы можете задать свой вопрос "
                         f"и вам ответит первый освободившийся оператор в кратчайшие сроки!\n\n"
                         f"Рад был Вам помочь {message.from_user.first_name}\n\n"
                         f"Если нужна будет моя помощь - то нажмите круглешок слева в этом чате "
                         f"и нажмите /start",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(contains="Завершить работу"))
async def close_app(message: types.Message):
    await message.answer(f"{message.from_user.first_name} Вы завершили работу\n"
                         f"Если хотите продолжить работу с ботом - нажмите на - /start",
                         reply_markup=types.ReplyKeyboardRemove())


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.reply(f'{message.from_user.first_name}, выбери пожалуйста какую-нибудь '
                        f'команду из меню! Спасибо \n\n'
                        f'В ближайшее время я научусь говорить '
                        f'с тобой на любые тему, ну а пока могу '
                        f'работать по запланированному сценарию')


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
