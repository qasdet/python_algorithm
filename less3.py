from memory_profiler import profile, memory_usage

# Курс Основы Python lesson_2 task_3

# До оптимизации


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        func(args[0], **kwargs)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Общий размер: {mem_diff}')
    return wrapper


@decor
@profile
def corrected(data):
    for element in data:
        employee_info = element.split()
        name_employee = employee_info[len(employee_info) - 1]
        correct_name = name_employee.capitalize()
        print(f'Привет {correct_name}')


list_employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                  'токарь высшего разряда нИКОЛАй', 'директор аэлита']

corrected(list_employees)

# После оптимизации


@decor
@profile
def corrected(data):
    for element in data:
        employee_info = element.split()
        name_employee = employee_info[len(employee_info) - 1]
        correct_name = name_employee.capitalize()
        print(f'Привет {correct_name}')


list_employees = ('инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                  'токарь высшего разряда нИКОЛАй', 'директор аэлита')

corrected(list_employees)
del list_employees
