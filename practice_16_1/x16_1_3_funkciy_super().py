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
    # raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def apply_raise(self):
        self.pay = int(self.pay * 1.1)


dev1 = Developer(first='Petr', last='Petrov', pay=50000, prog_lang='python')
print(dev1.first)
print(dev1.last)
print(dev1.pay)
print(dev1.prog_lang)