"""
Задача
Реализовать магический метод add и добавить проверку на сложение только
с другими экземплярами класса Employee и дочерних классов.
"""

from builtins import isinstance


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

    def __add__(self, other):
# проверяем объект принадлежащий классу,
# если является сущностью класса либо его наследником - True, self.__class__ - ссылка на класс
        if isinstance(other, self.__class__):
            return self.pay + other.pay

        raise TypeError


class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


emp1 = Employee('Ivan', 'Ivanov', 50000)
dev1 = Developer('Petr', 'Petrov', 50000, 'python')

res = emp1 + dev1
print(res)


class ExampleClass:
    pass



