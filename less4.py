from pympler.asizeof import asizeof
from numpy import array

# Курс основы Python lesson_5 task_4
# До оптимизации


def l_c(lst):
    list_number = [number for number in (src[1:]) if number > src[src.index(number) - 1]]
    print(f'Размер до оптимизации: {asizeof(list_number)}')


src = [300, 2, 12, 44, 1, 4, 10, 7, 1, 78, 123, 55]
l_c(src)

# После оптимизации


def l_c(lst):
    list_number = array([number for number in (src[1:]) if number > src[src.index(number) - 1]])
    print(f'Размер после оптимизации: {asizeof(list_number)}')


src = [300, 2, 12, 44, 1, 4, 10, 7, 1, 78, 123, 55]
l_c(src)


"""
Прибегнув к модулю Numpy в половину сократил расходы памяти на массив
Размер до оптимизации: 312
Размер после оптимизации: 152
"""