import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp, db, bot
from keyboards.default.menu import menu


@dp.message_handler(CommandStart(),state="*")
async def bot_start(message: types.Message,state:FSMContext):
    name = message.from_user.full_name
    # Добавляем пользователей в базу
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"Добро пожаловать! {name}\n\n"
                             f"🤖 Я бот который поможет тебе заказать кожаные изделия от G.P.AND\n\n"
                             f"🤝 Заказать похожего или совсем иного бота? Свяжитесь с разработчиком <a href='https://t.me/zufar_ik'>Zufar</a>",
                             reply_markup=menu)

        # Оповещаем админа
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} добавлен в базу пользователей.\nВ базе есть {count} людей."
        await bot.send_message(chat_id=ADMINS[1], text=msg)
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[1], text=f"{name} в базе имелся раньше")
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} в базе имелся раньше")
        await message.answer(f"Добро пожаловать! {name}\n\n"
                             f"🤖 Я бот который поможет тебе заказать кожаные изделия от G.P.AND\n\n"
                             f"🤝 Заказать похожего или совсем иного бота? Свяжитесь с разработчиком <a href='https://t.me/zufar_ik'>Zufar</a>",
                             reply_markup=menu)
    await state.finish()

