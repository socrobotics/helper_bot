from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Начать работу с ботом"),
            types.BotCommand("shop_telega", "Перейти в телеграм магазин FB аккаунтов"),
            types.BotCommand("shop_site", "Перейти на сайт в магазин FB аккаунтов"),
            types.BotCommand("channels", "Список каналов на подписку"),
            types.BotCommand("create_post", "Предложить пост в канале"),
            types.BotCommand("convert_money", "Сконвертировать валюту"),
            types.BotCommand("help", "Задать вопрос в техподдержку"),
        ]
    )
