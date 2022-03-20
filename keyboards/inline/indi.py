from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

send_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Отправить",callback_data="send_to_admin")],
        [InlineKeyboardButton(text="Отменить",callback_data="stop")]
    ]
)

user = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Отправить",callback_data="send_to_admin")],
        [InlineKeyboardButton(text="Отмена",callback_data="cancel")]
    ]
)

contactnum = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Поделиться номером", request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Отправить",callback_data="send_to_channel")],
        [InlineKeyboardButton(text="Отмена",callback_data="cancel")]
    ]
)