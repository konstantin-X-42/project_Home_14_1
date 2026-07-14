"""
Задача
Для магического метода __add__ класса Employee добавить обработку исключений при передаче в метод значений,
которые должны быть объектами этого же класса или числом. Написать тесты на обработку исключений.

Флоу решения:
1. Восстановить класс Employee
2. Написать проверку значений и возбуждать исключение
3. Написать тесты на обработку возникающих исключений
"""

# raise TypeError конструкция останавливает программу и выбрасываем исключение


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        elif isinstance(other, (int, float)):
            return self.pay + other
        raise TypeError


if __name__ == "__main__":
    emp_1 = Employee(first="Ivan", last="Ivanov", pay=50000)
    emp_2 = Employee(first="Petr", last="Petrov", pay=50000)

    print(emp_1 + emp_2)
    print(emp_1 + 10000)
    print(emp_1 + "123123")

# ===================================================
# тестирование
# ===================================================

import pytest

#
# from main import Employee


def test_raises():
    emp_1 = Employee(first="Ivan", last="Ivanov", pay=50000)
    with pytest.raises(TypeError) as e_info:
        emp_1 + "50000"


def test_raises_with_dict():
    emp_1 = Employee(first="Ivan", last="Ivanov", pay=50000)
    with pytest.raises(TypeError) as e_info:
        emp_1 + {"1": "2"}  # размещаем только строку кода гдне исключение!!


# делаем отдельные тесты на конструктор
