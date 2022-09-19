def sum_number(num_1, num_2):
    total = hex(num_1 + num_2)
    return list(str(total).upper())[2:]

def mul_number(numb_1, numb_2):
    total = hex(numb_1 * numb_2)
    return list(str(total).upper())[2:]


def calculation_number():
    user_inp_1 = list(input('Введите число в 16-ной системе: '))
    user_inp_2 = list(input('Введите второе число в 16-ной системе: '))
    number_1 = int(''.join(user_inp_1), 16)
    number_2 = int(''.join(user_inp_2), 16)
    print(f'Сумма чисел: {sum_number(number_1, number_2)}')
    print(f'Произведение чисел: {mul_number(number_1, number_2)}')


if __name__ == '__main__':
    calculation_number()



class CalcNum:
    def __init__(self, num):
        self.num = int(''.join(num), 16)

    def __add__(self, other):
        total = str(hex(self.num + other.num))[2:].upper()
        return list(total)

    def __mul__(self, other):
        total = str(hex(self.num * other.num))[2:].upper()
        return list(total)


user_1 = list(input('Введите число в 16-ной системе: '))
user_2 = list(input('Введите второе число в 16-ной системе: '))

num_one = CalcNum(user_1)
num_two = CalcNum(user_2)

print(num_one + num_two)
print(num_one * num_two)