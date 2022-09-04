'''4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.'''

num = int(input("Введите  целое число"))
def rec(a=.0, b=0, count=1, summ=.0):
    return rec(a=1*(-0.5) ** (count - 1), summ=summ+a, count=count + 1, b=b)\
        if count <= num + 1 else print(summ)
rec(a=0, b=0, count=1, summ=0)