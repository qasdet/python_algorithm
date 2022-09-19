import statistics
from random import randint
from timeit import timeit


m = 10
obj_list = [randint(1, 100) for _ in range(2*m+1)]
print(statistics.median(obj_list[:]))
print(timeit("statistics.median(obj_list[:])", globals=globals(), number=1000))

m = 100
obj_list = [randint(1, 100) for _ in range(2*m+1)]
print(statistics.median(obj_list[:]))
print(timeit("statistics.median(obj_list[:])", globals=globals(), number=1000))

m = 1000
obj_list = [randint(1, 100) for _ in range(2*m+1)]
print(statistics.median(obj_list[:]))
print(timeit("statistics.median(obj_list[:])", globals=globals(), number=1000))



"""
Сортировка Шелла
10 элементов - 0.010733800000000009
100 элементов - 0.2118982
100 элементов - 3.2464531
Без сортировки
10 элементов - 0.005489000000000001
100 элементов - 0.263112
1000 элементов - 19.9983702
Встроенная функция statistics
10 элементов - 0.0006145999999999999
100 элементов - 0.006121299999999996
1000 элементов - 0.16989
Встроенные функции работаю намного быстрее
До 100 элементов можно обойтись и без сортировки, но всегда лучше пользоваться встроенными функциями. т.к они уже оптимизированы
"""