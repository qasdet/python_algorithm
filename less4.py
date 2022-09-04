import hashlib

salt = 'my_salt'


def func(adress, dct={}):
    try:
        return dct[adress]
    except KeyError:
        dct.update({adress: hashlib.sha512(adress.encode() + salt.encode()).hexdigest()})
        return "Хеш вычислен и записан в кеш!!"


print(func("https://yandex.ru/"))
print(func("https://yandex.ru/"))
print(func("https://gb.ru/"))


def func(adress, dct={}):
    return dct.setdefault(adress, hashlib.sha512(adress.encode() + salt.encode()).hexdigest())


print(func('https://gb.ru/'))
print(func('https://gb.ru/'))
print(func('https://yandex.ru/'))
print(func('https://yandex.ru/'))
