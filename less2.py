from pympler.asizeof import asizeof


# Курс Основы Python lesson_9 task_2

# До оптимизации


# class Worker:
#
#     def __init__(self, name, surname, position, income):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = dict(income)
#
#
# class Position(Worker):
#     def get_full_name(self):
#         print(f'Работник: {self.surname} {self.name} \n'
#               f'Должность: {self.position}')
#
#     def get_total_income(self):
#         total_income = self._income['wage'] + self._income['bonus']
#         print('Полный доход составляет: ', total_income)
#
#
# worker = Position('Иван', 'Иванов', 'механик', {'wage': 10000, 'bonus': 20000})
# print(f'Размер объекта до оптимизации: {asizeof(worker)}')


# После оптимизации

class Worker:
    __slots__ = 'name', 'surname', 'position', '_income'

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict(income)


class Position(Worker):
    def get_full_name(self):
        print(f'Работник: {self.surname} {self.name} \n'
              f'Должность: {self.position}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print('Полный доход составляет: ', total_income)


worker = Position('Иван', 'Иванов', 'механик', {'wage': 10000, 'bonus': 20000})

print(f'Размер объекта после оптимизации: {asizeof(worker)}')

"""
В с помощью __slots__ экономлю память, расширять атрибуты класса не планирую,
поэтому имеет смысл задействовать этот метод
Размер объекта до оптимизации: 1056
Размер объекта после оптимизации: 856
"""
