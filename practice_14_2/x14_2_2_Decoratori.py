def printing(func):  # передаём в декоратор функцию

    # inner вызывает итоговую функцию с аргументами *args, **kwargs для универсальности аргументов
    def inner(*args, **kwargs):  # вложенная функция inner или wrapper, передаются арг-ты из new_f(10)
        """
        args - это позиционные аргументы, список list, * распаковка args,
        kwargs - это аргументы по ключам, словарь dict, ** распаковка kwargs
        ПРИМЕР: my_func(1, 2, 3, 4, 5, x=1, y=2, z=3)
        1, 2, 3, 4, 5 - позиционные аргументы в декораторе преобразуются в список list и будут лежать в переменной args
        x=1, y=2, z=3 аргументы в декораторе преобразуются в словарь dict и доступны по ключу в переменной **kwargs
        """
        result = func(*args, **kwargs)
        print(f"функция {func} вызывается с результатом {result}")
        return result  # результат выполнения функции new_f(10)

    return inner  # возвращаем ссылку на функцию


@printing  # оборачивает add_one декоратор он вызывает ф-ю inner сокращённая запись
# функция для декорирования
def add_one(x):
    return x + 1


# без @printing нужна строка
# new_f = printing(add_one)  # передаём ссылку на функцию (без скобок)

y = add_one(10)

# без @printing нужна строка
# y = new_f(10)  # вызываем функцию

print(y)

# >>> 11


# ================================
print("\n==  random  ==\n")
# ================================
import random

"""
Создаём декоратор который оборачивает функцию и возвращает целое число случайных чисел random
"""


def my_decorator(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        result_int = int(result)  # модификация вызова функции
        return result_int

    return inner


@my_decorator
def get_rand_numbers():
    return random.randint(1, 100) / random.randint(1, 100)


print(get_rand_numbers())

# ================================
print("\n==  УНИВЕРСАЛЬНЫЙ ДЕКОРАТОР ЗАМЫКАНИЕ  ==\n")
# ================================


# Декораторы функций
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("------ что-то делаем перед вызовом функции ------")
        res = func(*args, **kwargs)
        print("------ что-то делаем после вызова функции ------")
        return res

    return wrapper


def some_func(title, tag):
    print(f"title = {title}, tag = {tag}")
    return f"<{tag}>{title}</{tag}>"


some_func = func_decorator(some_func)
res = some_func("Python навсегда!", "h1")
print(res)

# >>> ------ что-то делаем перед вызовом функции ------
# >>> title = Python навсегда!, tag = h1
# >>> ------ что-то делаем после вызова функции ------
# >>> <h1>Python навсегда!</h1>
