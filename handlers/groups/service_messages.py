from aiogram import types

from filters import IsGroup
from loader import dp, bot


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f'✋Добро пожаловать, <b>{members}</>\n\n'
                        f'🔎🤫 Здесь <b>@SocroboticStoreBot</> ты найдешь отличные аккаунты под запуск рекламы!\n\n'
                        f'<b>В этом чате можешь обсуждать вопросы связанные с facebook</>\n\n'
                        f'Команда саппортов, которая ответит на любой твой вопрос:\n\n'
                        f"<b>По вопросам связанным с аккаунтами:</>\n"
                        f'@eduardnos\n'
                        f'@mamaevmaksi\n'
                        f'@viktoriavergi\n\n'
                        f"<b>По вопросам связанным с софтом:</>\n"
                        f'@clever_ded\n'
                        f'@pharaon93rus\n\n'
                        f"<b>По вопросам связанным с прокси:</>\n"
                        f'@Mountain_man_proxy\n\n'
                        f'Общий чат технической поддержки <b>@SocroboticHelp_bot</> - 24/7\n\n'
                        f'<b>По крайне важным вопросам писать админу - @makarovdenis89</>\n\n'
                        f'Запрещены:\n'
                        f'-оскорбления\n'
                        f'-мат\n'
                        f'-флуд\n'
                        f'-спам\n'
                        f'-реклама без согласия администрации\n'
                        f'-порнография = <b>БАН</>\n')


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def left_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f'{message.left_chat_member.get_mention(as_html=True)} '
                             f'вышел из чата')
    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.answer(f'{message.left_chat_member.get_mention(as_html=True)} был удален из чата'
                             f' пользователем {message.from_user.get_mention(as_html=True)}')
