import time


def function(func):
    def wrapped(*args, **kwargs):
        start_time = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            print(f'Операция  {func.__name__} заняла {(time.time() - start_time) * 1000} сек')

    return wrapped


lst_2 = []
lst_3 = []
dct_2 = {}


@function
def lst_appnd(n):  # O(n)
    for i in range(1, n + 1):  # O(n)
        lst_2.append(i)  # O(1)


lst_appnd(100000)


@function
def lst_insrt(n):  # O(n^2)
    for i in range(1, n + 1):  # O(n)
        lst_3.insert(0, 1)  # O(n)


lst_insrt(100000)


@function
def dct_add(n):  # O(n)
    for i in range(1, n + 1):  # O(n)
        dct_2[i] = 1  # O(1)


dct_add(100000)
"""Cложность в O-нотации для заполнения списка функцией append- O(n), 
заполнение словаря также имеет сложность #O(n). Однако при использовании функции insert(если 
вставлять значение в начало списка) сложность- O(n^2). Замер времени показывает, что заполнение списка
при помощи append немного быстрее, чем заполнение словаря, но при использовании insert(вставка в начало списка)
тратится значительно больше времени.
"""


@function
def get_lst_el(lst):  # O(n)
    for idx, i in enumerate(lst):  # O(n)
        return lst[idx]  # O(1)


get_lst_el(lst_2)


#
@function
def get_dct_el(dct):  # O(n)
    for key in dct:  # O(n)
        return dct[key]  # O(1)


get_dct_el(dct_2)
"""Получение элемента словаря значительно быстрее, чем элемента списка. Но обе функции имеют сложность O(n)"""


@function
def pop_out_lst(lst):  # O(n)
    while lst:  # O(n)
        return lst.pop()  # O(1)


pop_out_lst(lst_2)


@function
def pop_out_dct(dct):  # 0(n)
    for key in dct:  # O(n)
        return dct.pop(key)  # O(1)


pop_out_dct(dct_2)
"""Операция pop также значительно быстрее в словарях. """
