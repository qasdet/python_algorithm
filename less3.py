'''3. Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран. Например, если введено число 3486, то надо вывести
число 6843.'''


num = int(input("Введите  целое число"))
def rec(count=0, a=10, b=1, digit=0, res=''):
    if count < len(str(num)):
        digit = str(num % a // b)
        res = str(res + digit)
        return rec(count=count + 1, a=a * 10, b=b * 10, res=res)
    # print(res)
    return res
