"""
Задача
- Создать класс для разработчиков, установить ставку индексации ЗП 10%.
- Создать двух разработчиков.

Задача
Создание класса Developer.

Флоу решения:
1.Создать класс, наследуемый от базового
2.Переопределить атрибут класса
3.Создать два экземпляра класса
"""

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


# class Developer(Employee): # класс унаследует все атрибуты и функции от родительского класса, несмотря на pass
#     pass


class Developer(Employee):
    raise_amt = 1.1  # внутри класса Developer переопределяем атрибут родительского класса raise_amt

# ==================
print('\nуровень зарплаты обычного сотрудника')
#===================
emp1 = Employee('Ivan', 'Ivanov', 50000)
print(emp1.pay)  # <<< 50000
print(emp1.fullname()) # <<< Ivan Ivanov

# ==================
print('\nуровень зарплаты обычного сотрудника с коэф-ом повышения')
#===================
emp1.apply_raise()
print(emp1.pay)  # <<< 52000
print(emp1.fullname()) # <<< Ivan Ivanov

# ==================
print('\nуровень зарплаты разработчика')
#===================
dev1 = Developer('Petr', 'Petrov', 50000)  # с переопределением одного атрибута
print(dev1.pay)  # <<< 50000
print(dev1.fullname()) # <<< Petr Petrov

# ==================
print('\nуровень зарплаты разработчика с коэф-ом повышения')
#===================
dev1.apply_raise()
print(dev1.pay)  # <<< 55000
print(dev1.fullname()) # <<< Petr Petrov



