'''1. Написать программу, которая будет складывать, вычитать, умножать или
делить два числа. Числа и знак операции вводятся пользователем. После
выполнения вычисления программа не должна завершаться, а должна запрашивать
новые данные для вычислений. Завершение программы должно выполняться при вводе
символа '0' в качестве знака операции. Если пользователь вводит неверный знак
(не "0", "+", "-", "*", "/"), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции. Также сообщать пользователю о невозможности
деления на ноль, если он ввел 0 в качестве делителя.'''


class MyException(Exception):
    pass

def rec():
    try:
        a = int(input("Введите число 1:"))
        b = int(input("Введите число 2:"))
        sign = input("Введите один знак операции с числами - '+', '-', '*' или '/',"
                 " для выхода из программы введите '0' :")
        if sign != '0':
            if sign not in('+', '-', '/', '*'):
                raise MyException("wrong sign")
            if sign == '+':
                print(a + b)
            elif sign == '-':
                print(a - b)
            elif sign == '*':
                print(a * b)
            elif sign == '/':
                if b != 0:
                    print(a / b)
                else:
                    raise ZeroDivisionError("You can not divide by zero")
            return rec()
    except MyException as e:
        print("Ошибка! Введен неправильный знак операции!")
    except ValueError:
        print('Вы вместо числа ввели строку ((( Исправьтесь!')
    except ZeroDivisionError:
        print("Число два не должно быть равно 0! На ноль делить нельзя!")
    return rec()
rec()