price = {
    "Кошелёк из кожи женский": 150000, #+
    "Кошелёк из кожи мужской": 180000, #+
    "Бананка из кожи": 350000,#+
    "Портмоне из кожи": 350000,#+
    "Ключница из кожи": 130000,#+
    "Картхолдер из кожи":80000,
    "Обложка для паспорта из кожи":80000,
    "Документница из кожи" : 230000
}

def get_price(name, amount):
    narx = price[name]
    return int(narx) * int(amount)