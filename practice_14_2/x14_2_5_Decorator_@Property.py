# Инкапсуляция и управление доступом с помощью свойств (Property: Getter, Setter, Deleter)
# ======================================
# --  ДЕКОРАТОР @property  --
# ======================================
from practice_14_2.x14_2_3_class_static_metodi import first


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # ================================
    # 1. ГЕТТЕР (внутри класса сначало идет геттер затем сеттер)
    # ================================
    @property
    def fullname(self):
        """Возвращает полное имя сотрудника. К атрибуту можно обращаться без ()."""
        return f'{self.first} {self.last}'

    # ================================
    # 2. СЕТТЕР
    # ================================
    @fullname.setter
    def fullname(self, name):
        """Метод срабатывает при операции присваивания."""
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # ================================
    # 3. ДЕЛЕТЕР
    # ================================
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


# ================================
# ПРОВЕРКА РАБОТЫ (код для запуска)
# ================================

emp_1 = Employee('Иван', 'Иванов')

print("== Тест Геттера ==")
print(emp_1.fullname)  # Выведет: Иван Иванов (без скобок!)

print("\n== Тест Сеттера ==")
emp_1.fullname = 'Петр Петров'  # Срабатывает сеттер и делит строку по пробелу
print(emp_1.first)     # Выведет: Петр
print(emp_1.last)      # Выведет: Петров

print("\n== Тест Делетера ==")
del emp_1.fullname     # Выведет: Delete Name!
print(emp_1.first)     # Выведет: None


# ================================
print("\n==  ЗАДАЧИ  ==")
# ================================
"""
Задачи
Реализовавать метод fullname:
1. Можно обращаться как к обычному атрибуту.
2. Возвращает имя и фамилию через пробел.
3. При присваивании строки с именем и фамилией обновляет соответствующие атрибуты.
4. Реализовать метод email:Возвращает email сотрудника.
5. Доступ к методу как к обычному атрибуту, без вызова.

Флоу решения:
1. Реализовать метод email.
2. Добавить методу email декоратор @property.
3. Реализовать метод fullname, возвращающий полное имя.
4. Добавить методу fullname декоратор @property.
5. Реализовать метод fullname, присваивающий атрибутам «имя» и «фамилия» значения из строки полного имени.
6. Добавить методу fullname декоратор @fullname.setter.
"""

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property    # объявляем декоратор, конвертирует в атрибут - в результат выполнения метода
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property  # декоратор ГЕТТЕР
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter  # декоратор СЕТТЕР, (создаётся через название ГЕТТЕР)
    def fullname(self, new_fn):
        first, last = new_fn.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter  # декоратор ДЕЛЕТЕР, (очистка объекта)
    def fullname(self):
        self.first = None  # Стираем имя, заменяя на "ничего"
        self.last = None   # Стираем фамилию, заменяя на "ничего"


# ================================
# ПРОВЕРКА РАБОТЫ (код для запуска)
# ================================
# ================================
print("==  1. флоу решение  ==\n")
# ================================
emp = Employee('Ivan', 'Ivanov')  # инициализируем данные пользователя через ГЕТТЕР

# print(emp.email())     # с скобками без объявления декоратора @property
# print(emp.fullname())  # с скобками без объявления декоратора @property

print(emp.email)     # >>> Ivan.Ivanov@email.com
print(emp.fullname)  # >>> Ivan Ivanov

# ================================
print("\n==  2. флоу решение  ==\n")
# ================================

emp.fullname = 'Petr Petrov'  # изменяем имеющиеся данные пользователя через СЕТТЕР
print(emp.fullname)      # >>> Petr Petrov
print("== Измененные данные ==")
print(emp.first)         # >>> Petr (имя успешно обновилось!)
print(emp.last)          # >>> Petrov (фамилия успешно обновилась!)
print(emp.email)         # >>> petr.petrov@email.com (email пересчитался автоматически!)

print("== Очистили данные ==")
del emp.fullname         # стираем имеющиеся данные пользователя через ДЕЛЕТЕР
print(emp.fullname)      # >>> None None