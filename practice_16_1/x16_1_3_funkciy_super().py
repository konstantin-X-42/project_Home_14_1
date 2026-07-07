class Employee:    # 1-й род.класс
    def work(self):
        print('Do some work')

class Developer(Employee):   # 2-й род.класс
    def work(self):
        super().work()  # передаёт 'Do some work' 1род.класса
        print('Write code')

class JavaDeveloper(Developer):
    def work(self):
        super().work()  # передаёт 'Write code' 2род.класса
        print('Write tests for code')

# --- ЗАПУСК КОДА ---
# 1. Создаем объект (экземпляр) класса JavaDeveloper
developer = JavaDeveloper()

# 2. Вызываем метод work() у этого объекта
developer.work()  # >>> Do some work
                  # >>> Write code
                  # >>> Write tests for code

# =========================================================
# Расширение методов родительского класса в дочернем классе
print("\n- РАСШИРЕНИЕ -")
# =========================================================

class Employee:
    def go_to_vacation(self):
        print('Go to vacation')

class Accountant(Employee):
    def go_to_vacation(self):
        """ Расширение """
        print('Pass documents')  # выводим расширение дочернего класса
        super().go_to_vacation() # выводим наследование от родительского класса

# --- Пример запуска ---
# Создаём объект бухгалтера
accountant = Accountant()

# Вызываем метод
accountant.go_to_vacation()
# >>> Pass documents
# >>> Go to vacation


# =========================================================
# Переопределение методов родительского класса в дочернем классе
print("\n- ПЕРЕОПРЕДЕЛЕНИЕ -")
# =========================================================

class Employee:
    def go_to_vacation(self):
        print('Go to vacation')

class Developer(Employee):
    def go_to_vacation(self):
        """ Переопределение """
        print('Go back to work, no vacation') # переопределяем метод вывода родительского класса

# --- Пример запуска ---
# Создаем объект разработчика
developer = Developer()

# Вызываем переопределенный метод
developer.go_to_vacation()
# >>> Go back to work, no vacation


# =========================================================
# Переопределение и расширение методов родительского класса в дочернем классе на практике
print("\n- ПЕРЕОПРЕДЕЛЕНИЕ и РАСШИРЕНИЕ -")
# =========================================================
"""
Задача
Добавить разработчикам атрибут «язык программирования».

Флоу решения:
1. Создать инициализатор
2. Вызвать super()
3. Дописать атрибут prog_lang
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


class Developer(Employee):
    raise_amt = 1.1  # переопределение атрибута в классе


    def __init__(self, first, last, pay, prog_lang):    # расширение функционала
        super().__init__(first, last, pay)   # через ф. super() передаём атрибуты с родительского класса
        # self.first = first # строка при использовании ф. super() НЕ НУЖНА
        # self.last = last # строка при использовании ф. super() НЕ НУЖНА
        # self.pay = pay # строка при использовании ф. super() НЕ НУЖНА
        self.prog_lang = prog_lang


print("- Сотрудник -")
emp1 = Employee('Ivan', 'Ivanov', 50000)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)


print("\n- Разработчик -")
dev1 = Developer('Petr', 'Petrov', 50000, 'python')
print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)
