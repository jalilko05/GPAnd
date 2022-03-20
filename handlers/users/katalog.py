from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu import category, count1, menu
from keyboards.inline.indi import send_admin
from keyboards.inline.product import koshelek1, koshelek2, bananka1, portmone1, kluch1, carth1, obloj1, doc1
from loader import dp, db
from states.state import Koshelek, Zakaz, Bananka, Portmone, Kluch, Cart, Oblojka, Document


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


@dp.message_handler(text="🛍Каталог",state="*")
async def cataloc(message: types.Message):
    await message.answer("Выберите категорию заказа", reply_markup=category)

@dp.message_handler(text="Отмена",state="*")
async def back1(message: types.Message, state: FSMContext):
    await message.answer("Вы отменили действие!",reply_markup=category)
    await state.finish()

@dp.message_handler(text="Картхолдеры и прочее")
async def cataloc(message: types.Message, state: FSMContext):

    await message.answer_photo(
        photo="https://ibb.co/Y06zvdz",
        caption="Бананка из кожи",
        reply_markup=bananka1)


    # await call.message.bot.delete_message(call.bot.id, call.message.message_id)
    photo = "https://ibb.co/smbSR9Q"
    await message.answer_photo(photo=photo,
                               caption="Ключница из кожи",
                               reply_markup=kluch1, )


    await message.answer_photo(photo="https://ibb.co/yyKXbcg",
                               caption="Картхолдер из кожи",
                               reply_markup=carth1, )



@dp.callback_query_handler(text="addobloj1")
async def koshel(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Выберите количество ниже", reply_markup=count1)
    namep1 = "Обложка для паспорта из кожи"
    await state.update_data(
        {"obloj1": namep1}
    )
    await call.message.delete()
    await Oblojka.oblojka1.set()


@dp.message_handler(state=Oblojka.oblojka1)
async def add1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        data = await state.get_data()
        NAME = data.get("obloj1")
        idname = message.from_user.id
        product = db.check_product(tg_id=message.from_user.id, Name=NAME)
        if product:
            db.update_product(tg_id=idname, Name=NAME, quantity=int(product[2]) + int(n))
        else:
            db.add_product(tg_id=idname, Name=NAME, quantity=n)
        await message.answer("Ваш заказ добавлен в корзинку!\n"
                             f"Ваш ID {idname}\n"
                             f"Название продукта {NAME}\n", reply_markup=menu)
        await state.finish()


@dp.callback_query_handler(text="adddoc1")
async def koshel(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("Выберите количество ниже", reply_markup=count1)
    named1 = "Документница из кожи"
    await state.update_data(
        {"doc1": named1}
    )
    await call.message.delete()
    await Document.doc1.set()


@dp.message_handler(state=Document.doc1)
async def add1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        data = await state.get_data()
        NAME = data.get("doc1")
        idname = message.from_user.id
        product = db.check_product(tg_id=message.from_user.id, Name=NAME)
        if product:
            db.update_product(tg_id=idname, Name=NAME, quantity=int(product[2]) + int(n))
        else:
            db.add_product(tg_id=idname, Name=NAME, quantity=n)
        await message.answer("Ваш заказ добавлен в корзинку!\n"
                             f"Ваш ID {idname}\n"
                             f"Название продукта {NAME}\n", reply_markup=menu)
        await state.finish()


@dp.callback_query_handler(text="addcart1")
async def koshel(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Выберите количество ниже", reply_markup=count1)
    namec1 = "Картхолдер из кожи"
    await state.update_data(
        {"cart1": namec1}
    )
    await call.message.delete()
    await Cart.cart1.set()


@dp.message_handler(state=Cart.cart1)
async def add1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        data = await state.get_data()
        NAME = data.get("cart1")
        idname = message.from_user.id
        product = db.check_product(tg_id=message.from_user.id, Name=NAME)
        if product:
            db.update_product(tg_id=idname, Name=NAME, quantity=int(product[2]) + int(n))
        else:
            db.add_product(tg_id=idname, Name=NAME, quantity=n)
        await message.answer("Ваш заказ добавлен в корзинку!\n"
                             f"Ваш ID {idname}\n"
                             f"Название продукта {NAME}\n", reply_markup=menu)
        await state.finish()


@dp.callback_query_handler(text="addklu1")
async def koshel(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("Выберите количество ниже", reply_markup=count1)
    namek1 = "Ключница из кожи"
    await state.update_data(
        {"kluch1": namek1}
    )
    await call.message.delete()
    await Kluch.kluch1.set()


@dp.message_handler(state=Kluch.kluch1)
async def add1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        data = await state.get_data()
        NAME = data.get("kluch1")
        idname = message.from_user.id
        product = db.check_product(tg_id=message.from_user.id, Name=NAME)
        if product:
            db.update_product(tg_id=idname, Name=NAME, quantity=int(product[2]) + int(n))
        else:
            db.add_product(tg_id=idname, Name=NAME, quantity=n)
        await message.answer("Ваш заказ добавлен в корзинку!\n"
                             f"Ваш ID {idname}\n"
                             f"Название продукта {NAME}\n", reply_markup=menu)
        await state.finish()


@dp.message_handler(text="Портмоне")
async def cataloc(message: types.Message, state: FSMContext):
    await message.answer_photo(
        photo="https://ibb.co/mRmWvLm",
        caption="Портмоне из кожи",
        reply_markup=portmone1)



@dp.callback_query_handler(text="addpor1")
async def koshel(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("Выберите количество ниже", reply_markup=count1)
    namep1 = "Портмоне из кожи"
    await state.update_data(
        {"portmone1": namep1}
    )
    await call.message.delete()
    await Portmone.portmone1.set()


@dp.message_handler(state=Portmone.portmone1)
async def add1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        data = await state.get_data()
        NAME = data.get("portmone1")
        idname = message.from_user.id
        product = db.check_product(tg_id=message.from_user.id, Name=NAME)
        if product:
            db.update_product(tg_id=idname, Name=NAME, quantity=int(product[2]) + int(n))
        else:
            db.add_product(tg_id=idname, Name=NAME, quantity=n)
        await message.answer("Ваш заказ добавлен в корзинку!\n"
                             f"Ваш ID {idname}\n"
                             f"Название продукта {NAME}\n", reply_markup=menu)
        await state.finish()


@dp.message_handler(text="Документницы")
async def cataloc(message: types.Message, state: FSMContext):
    await message.answer_photo(photo="https://ibb.co/4dnv4gq",
                               caption="Обложка для паспорта из кожи",
                               reply_markup=obloj1, )

    await message.answer_photo(photo="https://ibb.co/ZzKJkhk",
                               caption="Документница из кожи",
                               reply_markup=doc1, )





@dp.callback_query_handler(text="addban1")
async def koshel(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("Выберите количество ниже", reply_markup=count1)
    nameb1 = "Бананка из кожи"
    await state.update_data(
        {"bananka1": nameb1}
    )
    await call.message.delete()
    await Bananka.bananka1.set()


@dp.message_handler(state=Bananka.bananka1)
async def add1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        data = await state.get_data()
        NAME = data.get("bananka1")
        idname = message.from_user.id
        product = db.check_product(tg_id=message.from_user.id, Name=NAME)
        if product:
            db.update_product(tg_id=idname, Name=NAME, quantity=int(product[2]) + int(n))
        else:
            db.add_product(tg_id=idname, Name=NAME, quantity=n)
        await message.answer("Ваш заказ добавлен в корзинку!\n"
                             f"Ваш ID {idname}\n"
                             f"Название продукта {NAME}\n", reply_markup=menu)
        await state.finish()


@dp.message_handler(text="Кошельки")
async def cataloc(message: types.Message, state: FSMContext):
    await message.answer_photo(
        photo="https://ibb.co/PtKYFGZ",
        caption="Кошелек из кожи женский", reply_markup=koshelek1)


    await message.answer_photo(
        photo="https://ibb.co/ZL1wVFB",
        caption="Кошелек из кожи мужской", reply_markup=koshelek2)





@dp.callback_query_handler(text="addkosh1")
async def koshel(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Выберите количество ниже", reply_markup=count1)
    namek1 = "Кошелёк из кожи женский"
    await state.update_data(
        {"koshelek1": namek1}
    )
    await call.message.delete()
    await Koshelek.koshelek1.set()


@dp.message_handler(state=Koshelek.koshelek1)
async def add1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        data = await state.get_data()
        NAME = data.get("koshelek1")
        idname = message.from_user.id
        product = db.check_product(tg_id=message.from_user.id, Name=NAME)
        if product:
            db.update_product(tg_id=idname, Name=NAME, quantity=int(product[2]) + int(n))
        else:
            db.add_product(tg_id=idname, Name=NAME, quantity=n)
        await message.answer("Ваш заказ добавлен в корзинку!\n"
                             f"Ваш ID {idname}\n"
                             f"Название продукта {NAME}\n", reply_markup=menu)
        await state.finish()


@dp.callback_query_handler(text="addkosh2")
async def koshel(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("Выберите количество ниже", reply_markup=count1)
    namek2 = "Кошелёк из кожи мужской"
    await state.update_data(
        {"koshelek2": namek2}
    )
    await call.message.delete()
    await Koshelek.koshelek2.set()


@dp.message_handler(state=Koshelek.koshelek2)
async def add1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        data = await state.get_data()
        NAME = data.get("koshelek2")
        idname = message.from_user.id
        product = db.check_product(tg_id=message.from_user.id, Name=NAME)
        if product:
            db.update_product(tg_id=idname, Name=NAME, quantity=int(product[2]) + int(n))
        else:
            db.add_product(tg_id=idname, Name=NAME, quantity=n)
        await message.answer("Ваш заказ добавлен в корзинку!\n"
                             f"Ваш ID {idname}\n"
                             f"Название продукта {NAME}\n", reply_markup=menu)
        await state.finish()


@dp.callback_query_handler(text="cancel")
async def back(call: types.CallbackQuery):
    await call.message.answer("Вы нажали Отмену", reply_markup=category)
    await call.message.delete()


@dp.message_handler(text="Назад◀️")
async def back1(message: types.Message, state: FSMContext):
    await message.answer("Вы нажали назад!", reply_markup=menu)
    await state.finish()


@dp.message_handler(text="🪡Индивидуальный заказ",state="*")
async def indi(message: types.Message):
    await message.answer("Опишите свой заказ")
    await Zakaz.opis.set()


@dp.message_handler(state=Zakaz.opis)
async def opis(message: types.Message, state: FSMContext):
    opis = message.text
    await state.update_data(
        {"opisanie": opis}
    )
    await message.answer("Отправьте фотографию для примера")
    Username = message.from_user.username
    await state.update_data(
        {"username": Username}
    )
    await Zakaz.next()


@dp.message_handler(content_types=['photo'], state=Zakaz.foto)
async def foto(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    await state.update_data(
        {"photo": photo}
    )
    data = await state.get_data()
    cap = data.get("opisanie")
    foto = data.get("photo")
    user = message.from_user.username
    await message.answer_photo(photo=foto, caption=f"{cap}\n Username: @{user}\nВсе верно?", reply_markup=send_admin)
    await Zakaz.next()


@dp.callback_query_handler(text="send_to_admin", state=Zakaz.admin)
async def send(call: types.CallbackQuery, state: FSMContext):
    data1 = await state.get_data()
    username = data1.get("username")
    cap = data1.get("opisanie")
    foto = data1.get("photo")
    await call.bot.send_photo(chat_id=1297546327, photo=foto, caption=f"{cap}\nUsername: @{username}")
    await call.bot.send_photo(chat_id=80386502, photo=foto, caption=f"{cap}\nUsername: @{username}")
    await state.finish()
