from random import randint
from timeit import timeit


def get_mediana(obj_list):

    temp = obj_list
    for i in range(len(obj_list) // 2):
        temp.remove(max(temp))
    return max(temp)


m = 10
obj_list = [randint(1, 100) for _ in range(2*m+1)]
print(get_mediana(obj_list[:]))
print(timeit("get_mediana(obj_list[:])", globals=globals(), number=1000))

m = 100
obj_list = [randint(1, 100) for _ in range(2*m+1)]
print(timeit("get_mediana(obj_list[:])", globals=globals(), number=1000))

m = 1000
obj_list = [randint(1, 100) for _ in range(2*m+1)]
print(timeit("get_mediana(obj_list[:])", globals=globals(), number=1000))