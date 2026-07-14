"""
Исключения. Блоки try/except
Исключение         Причина                   Пример
AttributeError     Ошибка атрибута           Попытка сослаться на несуществующий атрибут
NameError          Ошибка имени              Попытка использовать несуществующее имя переменной
ZeroDivisionError  Ошибка деления на ноль    1 / 0
FileNotFoundError  Ошибка отсутствия файла   Попытка открыть несуществующий файл
"""

"""
Задача
Спровоцировать и обработать исключения разных типов:
- NameError
- ZeroDivisionError
- FileNotFoundError

Флоу решения:
1. print(a)
2. 1/0
3. open('unknown_file')
"""

try:
    print(a)
except NameError:
    print("Обращение к несуществующей переменной")

try:
    1 / 0
except ZeroDivisionError:
    print("Нельзя делить на ноль")

try:
    open("some_file")
except FileNotFoundError:
    print("Файл не существует")


"""
Иерархия исключений

Base Exception
│ 
├── KeyboardInterrupt
│ 
├── Exception
│   ├── AttributeError
│   │ 
│   ├── ArithmeticError
│   │   ├── ZeroDivisionError
│   │   ├── FloatingPointError
│   │   └── OverflowError
│   │
│   ├── AssertionError
│   │
│   ├── RuntimeError
│   │   ├── NotImplementedError
│   │   └── RecursionError
│   │
│   ├── NameError
│   │
│   ├── OSError
│   │   ├── FileNotFoundError
│   │   ├── InterruptedError
│   │   ├── PermissionError
│   │   └── TimeOutError
│   │
│   ├── TypeError
│   │
│   └── ValueError
│
├── SystemExit
│ 
└── GeneratorExit
"""
# ======================================================
print("\n- - Полная форма try/except - -")
# ======================================================

try:
    print("Основной код.")
except:
    print("Код, если возникло исключение.")
else:
    print("Код, если не возникло исключений.")
finally:
    print("Код, который выполняется всегда.")

# ======================================================
print("\n- - Исключения - -")
# ======================================================
# ИСКЛЮЧЕНИЯ в первую очередь пишем самые «далёкие» от корня исключения (самых младших «детей»/«внуков»),
# а самые близкие к Exception (или сам Exception) — в самый конец

try:
    a, b = input("Введите 2 числа через пробел: ").split()
    a, b = int(a), int(b)
    result = a / b
except ValueError as e:  # если вместо ValueError написать Exception, то ZeroDivisionError не когда не выполнится
    # Exception выводит исключения ниже по иерархии
    print(e)
except ZeroDivisionError as e:
    print(e)
else:  # если ошибок в блоке try нет (except не выводится), то срабатывает после try блок else
    print(result)
finally:
    print("Операция завершена")

# ======================================================
print("\n- - Задача - -")
# ======================================================

"""
Задача
Принять на вход от пользователя два числа a и b. 
Разделить a на b. Убедиться, что пользователь ввел числа и эти числа целые. 
Число b должно быть отличным от нуля.

Флоу решения:
1. Получить данные от пользователя
2. Обработать исключение ошибки ввода
3. Обработать исключение деления на ноль
"""

try:
    a, b = input("Введите 2 числа через пробел: ").split()  # <<< 25 2
    a, b = int(a), int(b)
    result = a / b
except ValueError as e:  # в "e" содержится информация об ошибке, "e" внедряют в систему логирования или
    # в файл, телеграмм канал или почту
    print(e)  # >>> unsupported operand type(s) for /: 'str' and 'str'

except ZeroDivisionError as e:
    print(e)  # >>> division by zero
else:  # выполняется если код отрабатывает по try
    print(result)  # >>> 12.5

finally:  # выполняется в любом случае завершения по except или try
    print("Операция завершена")  # >>> Операция завершена
