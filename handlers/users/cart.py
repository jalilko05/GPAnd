import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from handlers.users.price import get_price
from keyboards.default.menu import menu, category
from keyboards.inline.indi import user, contactnum
from loader import dp, db
from states.state import Zakaz1


@dp.message_handler(text='🛒Корзинка',state="*")
async def korzina(message: types.Message):
    products1 = db.get_products(tg_id=message.from_user.id)
    if len(products1) != 0:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Заказать 🚚")
        products = db.get_products(tg_id=message.from_user.id)
        total = 0
        msg = "Ваши заказы\n\n"
        for product in products:
            markup.add(f"❌ {product[1]} ❌")
            price = get_price(product[1], product[2])
            total += price
            msg += f"{product[1]} x {product[2]} = {price} сум\n"
        msg += f"\nОбщая сумма: {total} сум"
        markup.row("Назад", "Очистить 🗑")
        await message.answer(msg, reply_markup=markup)
    else:
        await message.answer("Ваша корзинка еще пуста! Может быть это исправим?", reply_markup=category)


@dp.message_handler(text_contains="❌")
async def delete_product(message: types.Message):
    product = message.text
    product = product.replace("❌", "")
    db.delete_product(tg_id=message.from_user.id, Name=product.strip())
    await message.answer(f"{product.strip()}! Удалена из корзинки!", reply_markup=menu)


@dp.message_handler(text="Очистить 🗑")
async def clearcart(message: types.Message):
    id = message.from_user.id
    db.clear_cart(tg_id=id)
    await message.answer("Ваша корзинка очищена!", reply_markup=menu)


@dp.message_handler(text="Назад")
async def back(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=menu)

@dp.message_handler(text="Заказать 🚚")
async def send(message: types.Message):
    products = db.get_products(tg_id=message.from_user.id)
    total = 0
    msg = "Ваши заказы\n\n"
    for product in products:
        price = get_price(product[1], product[2])
        total += price
        msg += f"{product[1]} x {product[2]} = {price} сум\n"
    msg += f"\nОбщая сумма: {total} сум"
    yes_no = ReplyKeyboardMarkup(resize_keyboard=True)
    yes_no.add("Да!")
    yes_no.add("Нет!")
    await message.answer(msg)
    await message.answer("Все верно?", reply_markup=yes_no)


@dp.message_handler(text="Да!")
async def yes(message: types.Message):
    await message.answer("Заполните нужные пункты пожалуйста", reply_markup=ReplyKeyboardRemove())
    await message.answer("Как вас зовут?")
    await Zakaz1.name.set()


@dp.message_handler(state=Zakaz1.name)
async def name(message: types.Message, state: FSMContext):
    id1 = message.from_user.id
    await state.update_data(
        {"id":id1}
    )
    name = message.text
    await state.update_data(
        {"name": name}
    )
    await message.answer("Введите адрес доставки")
    await Zakaz1.next()


@dp.message_handler(state=Zakaz1.Adress)
async def adress(message: types.Message, state: FSMContext):
    adress1 = message.text
    await state.update_data(
        {"adress": adress1}
    )
    await message.answer("Введите основной номер!", reply_markup=contactnum)
    await Zakaz1.next()


@dp.message_handler(content_types=['contact'], state=Zakaz1.tel)
async def get_img(message: types.Message, state: FSMContext):
    phone = message.contact['phone_number']
    num = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    if re.match(num, phone):
        await state.update_data(
            {'phone': phone}
        )
        await message.answer("Введите второстепенный номер!\n"
                             "(если его нет отправьте любой знак)")
        await Zakaz1.next()
    else:
        await message.answer("Вы ввели некорректный номер\n"
                             "Введите еще раз!")
        await Zakaz1.tel


@dp.message_handler(state=Zakaz1.tel2)
async def get_img(message: types.Message, state: FSMContext):
    tel2 = message.text
    await state.update_data(
        {'tel2': tel2}
    )
    data1 = await state.get_data()
    name = data1.get("name")
    adress1 = data1.get("adress")
    telnum1 = data1.get("phone")
    telnum2 = data1.get("tel2")
    Username = message.from_user.username
    await state.update_data(
        {"username": Username}
    )
    username = data1.get("username")
    await message.answer(
        text=f"Имя и фамилия: {name}\n"
             f"Адрес: {adress1}\n"
             f"Основной номер: +{telnum1}\n"
             f"Username: @{Username}\n"
             f"Второстепенный: +{telnum2}", reply_markup=user
    )
    await message.answer("Далее мы дадим вам реквизиты!", reply_markup=menu)
    await Zakaz1.next()

@dp.callback_query_handler(text="cancel",state=Zakaz1.confirmP)
async def back(call: types.CallbackQuery):
    await call.message.answer("Вы отменили заказ!", reply_markup=menu)
    await call.message.delete()


@dp.callback_query_handler(text="send_to_admin", state=Zakaz1.confirmP)
async def sendadmin(call: types.CallbackQuery, state: FSMContext):
    data1 = await state.get_data()
    name = data1.get("name")
    adress1 = data1.get("adress")
    telnum1 = data1.get("phone")
    telnum2 = data1.get("tel2")
    id1 = data1.get("id")
    Username = call.message.from_user.username
    await state.update_data(
        {"username": Username}
    )
    username = data1.get("username")
    id3 = call.message.from_user.id
    products = db.get_products(tg_id=id1)
    total = 0
    msg = "Его заказы\n\n"
    for product in products:
        price = get_price(product[1], product[2])
        total += price
        msg += f"{product[1]} x {product[2]} = {price} сум\n"
    msg += f"\nОбщая сумма: {total} сум\n"
    await call.bot.send_message(chat_id=1297546327,
                                text=f"{msg}\n"
                                     f"Имя и фамилия: {name}\n"
                                     f"Адрес: {adress1}\n"
                                     f"Основной номер: +{telnum1}\n"
                                     f"Username: @{username}\n"
                                     f"Второстепенный: +{telnum2}"
                                )
    await call.bot.send_message(chat_id=80386502,
                                text=f"{msg}\n"
                                     f"Имя и фамилия: {name}\n"
                                     f"Адрес: {adress1}\n"
                                     f"Основной номер: +{telnum1}\n"
                                     f"Username: @{username}\n"
                                     f"Второстепенный: +{telnum2}\n"
                                     f"ID {id3}"
                                )
    await call.message.answer("Ваш заказ принят!\n"
                              "Реквизит для оплаты <code>8400490473169308</code>\n"
                              "Нажмите на номер карты чтобы скопировать\n"
                              f"<tg-spoiler>{id1}</tg-spoiler>\n<b>Введите этот текст в комментариях к оплате чтобы подтвердить ваш заказ</b>\n"
                              "В случае если вы забыли добавить комментарий напишите <a>https://t.me/alexandrgp</a>", reply_markup=menu)

    db.clear_cart(tg_id=id1)

    await state.finish()


@dp.message_handler(text="Нет!")
async def no(message: types.Message):
    await message.answer("Вы отменили заказ!", reply_markup=menu)
