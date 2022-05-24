from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Код отправлен"),
        ],
        [
            KeyboardButton(text="⛔️Завершить работу"),
        ]
    ],
    resize_keyboard=True
)
menu_close = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⛔️Завершить работу"),
        ]
    ],
    resize_keyboard=True
)
menu_again = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚧 Повторить"),
        ],
        [
            KeyboardButton(text="⛔️Завершить работу"),
        ]
    ],
    resize_keyboard=True
)
menu_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Задать вопрос боту помощнику"),
        ],
        [
            KeyboardButton(text="Пообщаться с тех поддержкой socrobotic"),
        ],
        [
            KeyboardButton(text="⛔️Завершить работу"),
        ]
    ],
    resize_keyboard=True
)
