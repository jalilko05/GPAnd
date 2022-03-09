from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍Каталог")],
        [KeyboardButton(text="🛒Корзинка"),KeyboardButton(text="🪡Индивидуальный заказ")]
    ],
    resize_keyboard=True
)


category = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Кошельки"),KeyboardButton(text="Документницы")],
        [KeyboardButton(text="Портмоне"),KeyboardButton(text="Картхолдеры и прочее")],
        [KeyboardButton(text="Назад◀️")]
    ],
    resize_keyboard=True
)

count1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1"), KeyboardButton(text="2"),
         KeyboardButton(text="3")],
        [KeyboardButton(text="4"), KeyboardButton(text="5"),
         KeyboardButton(text="6")],
        [KeyboardButton(text="7"), KeyboardButton(text="8"),
         KeyboardButton(text="9")],
        [KeyboardButton(text="Отмена")]
    ],
    resize_keyboard=True
)