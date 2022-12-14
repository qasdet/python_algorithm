"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
d = {'Tash': ['tash', 'activated'], 'Ivan': ['Ivan', 'not activated'],
     'Petr': ['petr', 'activated'], 'Masha': ['masha', 'not activated']}


def check(key, password):  # O(n)
    if key in d.keys() and password == d[key][0]:  # O(n) + O(1) = O(n)
        if d[key][1] == 'not activated':  # O(1)
            print(f'{key}, your login and password are okay'  # O(1)
                  f' but you need to finish registration!')
        else:
            print('Your login and password are okay!'  # O(1)
                  ' You can keep using our service!')
    else:
        print('Your login or password are incorrect! Please try again!')  # O(1)


# check('Masha', 'masha')

def check_2(key, password):  # О(n)
    try:
        for login, info in d.items():  # O(n)
            lst = d[key]  # O(1)
            if key == login and password == lst[0]:  # О(1)
                if lst[1] == 'activated':  # О(1)
                    return f'{key},your login and password are okay!' \
                           f'You can keep using our service!'  # О(1)
                else:
                    return f'{key}, your login and password are okay ' \
                           f'but you need to finish registration!'  # О(1)
    except KeyError:
        return 'Your login or password are incorrect! Please try again!'  # О(1)
    else:
        return 'Your login or password are incorrect! Please try again!'  # О(1)


# check_2('Tash', 'ash')

def check_3(key, password):  # O(1)
    if d.get(key) and password == d[key][0]:  # O(1)
        if d[key][1] == 'not activated':  # O(1)
            print(f'{key},your login and password are okay but'  # O(1)
                  f' you need to finish registration!')
        else:
            print(f'{key},your login and password are okay!'  # O(1)
                  ' You can keep using our service!')
    else:
        print('Your login or password are incorrect! Please try again!')  # O(1)


# check_3('Ivan', 'Ivan')


"""Первое и второе решения менее эффективны,их сложность О(n), третье решение имеет сложность O(1)"""
