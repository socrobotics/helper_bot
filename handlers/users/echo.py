import asyncio
from currency_converter import CurrencyConverter
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from handlers.users.get_code import get_code_kopeechka
from keyboards.inline.menu import menu, menu_close, menu_again
from loader import dp

import threading

token = []
email = []


@dp.message_handler(Text(contains="weather"))
async def close_app(message: types.Message):
    await message.answer(f"Немного позже доделаю, пока в разработке\n",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(contains="convert_money"))
async def close_app(message: types.Message):
    c = CurrencyConverter()
    result = c.convert(500, 'EUR', 'USD')
    await message.answer(f"500 Евро = {result} $\n",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(
    Text(equals=['бля', 'хуй', 'хуе', 'хуя', 'пизда', 'залупа', 'пидор', 'пидар', 'ебан', 'ебу', 'хуй', 'сука',
                 'долбаеб',
                 'гандон', 'уеба', 'уебо']))
async def moderator(message: types.Message):
    msg = await message.answer(f'Уважаемый <b>{message.from_user.full_name}</>\n'
                               f'В нашем чате запрещено выражаться матом!\n'
                               f'Выражай свои мысли более-менее культурно!\n'
                               f'Спасибо!',
                               reply_markup=types.ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler(Text(equals=["поддержка", "помощь"]))
async def close_app(message: types.Message):
    await message.answer(
        f"{message.from_user.first_name} Вы можете задать свой вопрос в нашу техподдержку @SocroboticHelp_bot\n\n"
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


@dp.message_handler(Text(contains="код с почты"))
async def close_app(message: types.Message):
    await message.answer(f"@SocroboticStoreBot - здесь ты сможешь получить код с почты в разделе <b>Услуги</>",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(equals=["купить софт", "софт"]))
async def close_app(message: types.Message):
    await message.answer(f"{message.from_user.first_name} задай ему - @pharaon93rus любой вопрос по софту",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(equals=["промокод", "скидка", "промик"]))
async def close_app(message: types.Message):
    await message.answer(
        f"{message.from_user.first_name} Вы можете задать свой вопрос в нашу техподдержку @SocroboticHelp_bot\n\n"
        f"И Вам выдадут персональный промокод",
        reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(contains="бновлени"))
async def close_app(message: types.Message):
    await message.answer(f"Рекомендую подписаться на наш канал по обновам - https://t.me/fb_update\n\n"
                         f"а так же можно скачивать с облака - https://cloud.mail.ru/public/hCTc/SFbcpLyLG",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(contains="нструкци"))
async def close_app(message: types.Message):
    await message.answer(f"Посмотреть все инструкции можно здесь https://t.me/socrobotic_manual\n\n"
                         f"а так же можно скачивать с облака текстовый мануал - https://cloud.mail.ru/public/ApFm/NWn5oE1Dd",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(contains="мануал"))
async def close_app(message: types.Message):
    await message.answer(f"Посмотреть все инструкции можно здесь https://t.me/socrobotic_manual\n\n"
                         f"а так же можно скачивать с облака текстовый мануал - https://cloud.mail.ru/public/ApFm/NWn5oE1Dd",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(contains="платёж"))
async def close_app(message: types.Message):
    await message.answer(f"Вы можете использовать следующие способы оплаты: \n\n"
                         f"УКР карта\n"
                         f"Монобанк\n"
                         f"5375 4141 0377 6216 Oleksandr Gerko\n\n"
                         f"Web Money\n\n"
                         f"Z158268821498\n\n"
                         f"Qiwi\n\n"
                         f"+79048489718\n"
                         f"+79676741496\n\n"
                         f"Capitalist\n\n"
                         f"U11140306\n"
                         f"E11140308\n\n"
                         f"USDT(TRC20): TAKzHXmmLxaYnjUfQLLykUiUWcPc8tRCJa\n"
                         f"BTC: 15BvSUL5fCSfKaio8fxLPTRZe4vhWM2sey\n"
                         f"Ethereum: 0x83832ed12488cb8b21ce9342d792dd5ecd438e6a\n\n"
                         f"P.S. После перевода отпиши саппорту - @SocroboticHelp_bot\n"
                         f"А лучше сначала напиши саппорту, первый свободный ответит и ты сможешь оплатить свой заказ \n",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(contains="buy_proxy"))
async def close_app(message: types.Message):
    await message.answer(f"{message.from_user.first_name} задай ему - @Mountain_man_proxy любой вопрос по прокси\n"
                         f"ГЕО: 🇷🇺 🇰🇿 🇵🇱 🇺🇦 🇦🇿",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(contains="прокси"))
async def close_app(message: types.Message):
    await message.answer(f"{message.from_user.first_name} задай ему - @Mountain_man_proxy любой вопрос по прокси\n"
                         f"ГЕО: 🇷🇺 🇰🇿 🇵🇱 🇺🇦 🇦🇿",
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
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     await message.reply(f'{message.from_user.first_name}, выбери пожалуйста какую-нибудь '
#                         f'команду из меню! Спасибо \n\n'
#                         f'В ближайшее время я научусь говорить '
#                         f'с тобой на любые тему, ну а пока могу '
#                         f'работать по запланированному сценарию')


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
# @dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     state = await state.get_state()
#     await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
#                          f"\nСодержание сообщения:\n"
#                          f"<code>{message}</code>")
