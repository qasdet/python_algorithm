"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import profile


def count_numbers(number, odd=0, even=0):
    if number == 0:
        return f'Количество чисел: чётных {even} , нечётных {odd}'
    else:
        num = number % 10
        if num % 2 == 1:
            odd += 1
        else:
            even += 1
        return count_numbers(number // 10, odd, even)


@profile
def my_func():
    user_num = int(input('Введите число: '))
    print(count_numbers(user_num))


my_func()
