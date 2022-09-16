from pympler.asizeof import asizeof
from json import loads, dumps
from memory_profiler import profile

# Скрипт с курса Алгоритмы lesson_1 task_4

# До оптимизации
data_users = {'usr1': ['12345', True], 'usr2': ['12g3', False], 'usr3': ['r345', True], 'usr4': ['1245', False]}


@profile
def account_validation_2(data, login, password):
    if data.get(login):
        if data[login][1]:
            if data[login][0] == password:
                return 'Добро пожаловать'
            else:
                return 'Неверный пароль'
        else:
            return 'Вы не авторизованы, авторизуйтесь'
    else:
        return 'Неверный логин'


if __name__ == '__main__':
    answer = account_validation_2(data_users, 'usr3', 'r345')
    print(f'{answer}')


# После оптимизации
dumped_dict = dumps(data_users)


@profile
def account_validation_2(data, login, password):
    out_dict = loads(data)
    del data
    if out_dict.get(login):
        if out_dict[login][1]:
            if out_dict[login][0] == password:
                return 'Добро пожаловать'
            else:
                return 'Неверный пароль'
        else:
            return 'Вы не авторизованы, авторизуйтесь'
    else:
        return 'Неверный логин'


if __name__ == '__main__':
    answer = account_validation_2(dumped_dict, 'usr3', 'r345')
    print(f'{answer}')

print(f'Размер словаря: {asizeof(data_users)}')
print(f'Размер JSON: {asizeof(dumped_dict)}')

"""
В самом коде оптимизации не добился, но 
в хранении данных имеет смысл
их хранить в JSON формате, если пользователей будет миллионы,
будет ощутимая разница
Размер словаря: 1024
Размер JSON: 152
"""