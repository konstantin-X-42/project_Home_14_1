"""
Задача
- Добавить пользовательское отображение класса при выводе информации на экран.
- Добавить отладочное отображение класса.
- Реализовать возможность сложения двух объектов.
- Реализовать подсчет длины полного имени через встроенную функцию len.

Флоу решения:
1. Реализовать метод __repr__
2. Реализовать метод __str__
3. Реализовать метод __add__
4. Реализовать метод __len__
"""


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

# 2. метод __str__
    def __str__(self):
        return f'{self.first} {self.last} ({self.pay})'

# 1. метод __repr__
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.first}", "{self.last}", {self.pay})'

# 3. метод __add__
    def __add__(self, other):
        return self.pay + other.pay

# 4. метод __len__
    def __len__(self):
        # return 0  # будет выводить указанное количество
        return len(f'{self.first} {self.last}')  # будет вводить длину имени с пробелом

# -----------------------------------------------------------------
emp_1 = Employee('Ivan', 'Ivanov', 50000)

print(emp_1)  # >>> Ivan Ivanov (50000)

s_emp = str(emp_1)


# ================================
print("\n 2. метод __str__")
# ================================
print(type(s_emp))  # >>> <class 'str'>
print(s_emp)  # >>> Ivan Ivanov (50000)


# ================================
print("\n 1. метод __repr__")
# ================================
print(repr(emp_1))  # >>> Employee("Ivan", "Ivanov", 50000)


# ================================
print("\n 3. метод __add__")
# ================================
emp_2 = Employee('Petr', 'Petrov', 60000)

sum_pay = emp_1 + emp_2
print(sum_pay)  # >>> 110000


# ================================
print("\n 4. метод __len__")
# ================================
print(len(emp_1))  # >>> 11
