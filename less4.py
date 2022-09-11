
from timeit import timeit
from collections import OrderedDict

o_dct = OrderedDict()
dct = dict()

print('Заполнение словарей')
print(timeit('for i in range(1000): o_dct[i] = i', globals=globals(), number=1000))
print(timeit('for i in range(1000): dct[i] = i', globals=globals(), number=1000))

print('Получение значений по ключу')
print(timeit('for i in range(1000): a = o_dct[i]', globals=globals(), number=1000))
print(timeit('for i in range(1000): b = dct[i]', globals=globals(), number=1000))

print('Удаление элемента')
print(timeit('for _ in range(10): o_dct.popitem()', globals=globals(), number=100))
print(timeit('for _ in range(10): dct.popitem()', globals=globals(), number=100))