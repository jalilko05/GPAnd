from aiogram.dispatcher.filters.state import State, StatesGroup


class Reklama(StatesGroup):
    reklama = State()


class Koshelek(StatesGroup):
    koshelek1 = State()
    koshelek2 = State()

class Bananka(StatesGroup):
    bananka1 = State()

class Portmone(StatesGroup):
    portmone1 = State()

class Kluch(StatesGroup):
    kluch1 = State()

class Cart(StatesGroup):
    cart1 = State()

class Oblojka(StatesGroup):
    oblojka1 =State()

class Document(StatesGroup):
    doc1 = State()



class Del(StatesGroup):
    DELL = State()


class Zakaz(StatesGroup):
    opis = State()
    foto = State()
    admin = State()

class Zakaz1(StatesGroup):
    name = State()
    Adress = State()
    tel = State()
    tel2 = State()
    confirmP =State()