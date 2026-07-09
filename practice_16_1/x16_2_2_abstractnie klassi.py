"""
Задача
Создать абстрактный класс Employeeи два дочерних класса Developer и Accountant.

Флоу решения:
1. Импортировать модуль abc
2. Создать класс Employee(ABC)
3. Создать в Employee методы с декоратором @abstractmethod
"""

from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def work(self):
        pass


class Develop(Employee):

    def work(self):
        print('Write some code')

    def code(self):
        pass


class Accountant(Employee):

    def work(self):
        print('Counting')


dev_1 = Develop()
acc_1 = Accountant()

print(dev_1)  #  >>> <__main__.Develop object at 0x00000192EB6A4D70>
print(acc_1)  #  >>> <__main__.Accountant object at 0x00000192EB6A4EC0>