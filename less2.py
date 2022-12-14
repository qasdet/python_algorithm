"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

lst = [5, 2, 6, 76, 1, 104, 0]


def bSort(array):  # Сложность: O(n) = O(1) + O(n) х O(n) + O(1) + O(1) + O(1) = O(n^2)
    length = len(array) - 1  # O(1)
    for j in range(length):  # O(n)
        for i in range(length - j):  # O(n)
            if array[i] > array[i + 1]:  # O(1)
                array[i], array[i + 1] = array[i + 1], array[i]  # O(1)
    return array[0]  # O(1)


def check_2(arr):  # Cложность: O(n) = O(1) + O(n) х O(1) + O(1) + O(1) = O(1 + O(n х 1) + 1 + 1 = O(n)
    min_ = arr[0]  # O(1)
    for el in arr:  # O(n)
        if el < min_:  # O(1)
            min_ = el  # O(1)
    return min_  # O(1)


# bSort(lst)
# check_2(lst)

'''Второе решение эффективнее, т. к. имеет сложность О(n),  а первое - O(n^2)'''
