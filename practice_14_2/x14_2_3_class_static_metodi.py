import datetime


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# ================================
print("\n==  ЗАДАЧИ  ==\n")
# ================================

"""
Задачи
1. Добавить класс-метод from_string для изменения атрибутов «имя», «фамилия» из полного имени.
2. Добавить класс-метод set_raise_amt для изменения атрибута класса, хранящего уровень индексации ЗП.
3. Добавить статический метод is_workday для определения рабочего дня.

Реализация методов from_string, set_raise_amt и is_workday.
Флоу решения:
1. Реализовать метод from_string с декоратором @classmethod.
2. Реализовать метод set_raise_amt с декоратором @classmethod.
3. Реализовать метод is_workday с декоратором @staticmethod.
"""


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay

    # 1.
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # 2.
    @classmethod
    def set_raise_amt(cls, new_raise_amt):
        cls.raise_amt = new_raise_amt

    # 3.
    @staticmethod  #  встроенный декоратор в Python
    def is_workday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        return True


# для проверки
# ================================
print("\n==  2.  ==\n")
# ================================

emp_1 = Employee(first="Jon", last="Snow", pay=50000)
emp_2 = Employee(first="Ivan", last="Ivanov", pay=60000)

print(Employee.raise_amt)  # изначальные данные

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# ================================
print("\n==  1.  ==\n")
# ================================

emp_str_1 = "Jon-Snow-70000"
emp_str_2 = "Ivan-Ivanov-30000"
emp_str_3 = "Elena-Nikitina-90000"

first, last, pay = emp_str_1.split("-")
new_emp_1 = Employee(first, last, pay)

# new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

# ================================
print("\n==  3.  ==\n")
# ================================
my_date = datetime.date(year=2023, month=1, day=31)
print(Employee.is_workday(my_date))
