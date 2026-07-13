"""
Распространение исключений

При возникновении ошибки появляется сообщение
и полный стек вызовов до точного места
возникновения исключения.

Call Stack (Стек вызовов)
────────────────────────────────────────
▲ [Стек вызовов растет, снизу вверх]
│
│   ┌───────────────┐
│   │   func3()     │
│   ├───────────────┤
│   │   func2()     │
│   ├───────────────┤  │
│   │   func1()     │  │ [Выбрасывается исключение,
│   ├───────────────┤  ▼  сверху вниз]
│   │   module()    │
│   └───────────────┘
────────────────────────────────────────
"""
"""
Задача
Написать класс с тремя методами, в одном из которых возникает исключение. 
Сделать обработку исключения на разных уровнях.

Флоу решения:
1. Реализовать класс
2. Прописать методы
3. Прописать блоки try/except
"""

class MyClass:

    def func1(self):
        # try:
        1 / 0
        # except ZeroDivisionError:
        #     print('На ноль делить нельзя')
        print('Работает метод func1')

    def func2(self):
        self.func1()
        try:
            print(a)
        except NameError:
            print('Несуществующая переменная')
        print('Работает метод func2')

    def func3(self):
        # try:                               # 1.2
        self.func2()
        # except ZeroDivisionError:          # 1.2
        #     print('На ноль делить нельзя') # 1.2
        print('Работает метод func3')


if __name__ == '__main__':
    # try:                               # 1.1
    my_obj = MyClass()
    my_obj.func3()  # вызываем метод func3 он func2 он func1 в func1 возникает исключение
    # except ZeroDivisionError:          # 1.1
    #     print('На ноль делить нельзя') # 1.1

"""
1. ведем идентификацию исключения в каком методе
1.1 дописываем try и except
1.2 затем переносим try и except в func3, проверяем в последнем методе func3, в 1.1 убираем
1.3 анологично переносим try и except в func2, проверяем в последнем методе func2, в 1.2 убираем
2. таким методом сужаем круг и выходим на исключение

так же нам показывает в выводе куда смотреть для определения исключения в консоле ниже:

Traceback (most recent call last):
  File "C:\Users\User\PycharmProjects\project_Home_14_1\practice_17_1\x17_1_3_isklycheniy.py", line 62, in <module>
    my_obj.func3()  # вызываем метод func3 он func2 он func1 в func1 возникает исключение
    ~~~~~~~~~~~~^^
  File "C:\Users\User\PycharmProjects\project_Home_14_1\practice_17_1\x17_1_3_isklycheniy.py", line 53, in func3
    self.func2()
    ~~~~~~~~~~^^
  File "C:\Users\User\PycharmProjects\project_Home_14_1\practice_17_1\x17_1_3_isklycheniy.py", line 44, in func2
    self.func1()
    ~~~~~~~~~~^^
  File "C:\Users\User\PycharmProjects\project_Home_14_1\practice_17_1\x17_1_3_isklycheniy.py", line 38, in func1
    1 / 0
    ~~^~~
ZeroDivisionError: division by zero

"""


