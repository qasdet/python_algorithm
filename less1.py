
from random import randint
from timeit import timeit


def bubble_sort(obj_list):
    for _ in range(0, len(obj_list)-1):
        for j in range(len(obj_list)-1):
            if(obj_list[j] < obj_list[j+1]):
                temp = obj_list[j]
                obj_list[j] = obj_list[j+1]
                obj_list[j+1] = temp
    return obj_list


obj_list = [randint(1, 1000) for i in range(5000)]

# print(obj_list)
bubble_sort(obj_list[:])


def bubble_sort_1(obj_list):
    swap = True
    counter = 0
    while(swap):
        swap = False
        for i in range(len(obj_list) - counter - 1):
            if obj_list[i] < obj_list[i+1]:
                obj_list[i], obj_list[i+1] = obj_list[i+1], obj_list[i]
                swap = True
        counter += 1
    return obj_list


bubble_sort_1(obj_list[:])

print(timeit("bubble_sort(obj_list[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_1(obj_list[:])", globals=globals(), number=1000))