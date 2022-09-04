"""
Задание 5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

def form(num=32, count=2):
    if num <= 127:
        if count <= 10:
            print(f'{num} - {chr(num)}', end=' ')
            return form(num=num+1, count=count+1)
        elif count > 10:
            count = 1
            print(f'{num} - {chr(num)}')
            return form(num=num + 1, count=count + 1)

form()