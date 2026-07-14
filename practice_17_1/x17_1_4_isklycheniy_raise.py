# пример пользовательского исключения


class MyException(Exception):
    """Пользовательский класс исключения"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Неизвестная ошибка."

    def __str__(self):
        return self.message


# =====================================================================
# =====================================================================
"""
Задача
Реализовать класс для работы со скриптами.
Реализовать свои классы исключений для обработки исключений, связанных с шелл-скриптами.

Флоу решения:
1. Создать класс исключения
2. Наследоваться от Exception
3. Прописать инициализатор для задания сообщения по умолчанию
"""


class ShellException(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Ошибка обработки скрипта"

    def __str__(self):
        return self.message


class ShellEmptyException(ShellException):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Скрипт пустой"


class ShellShebangException(ShellException):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Отсутствует шебанг"


class ShellScript:

    def __init__(self, content):
        if not content:
            raise ShellEmptyException()
        elif content[0:2] != "#!":
            raise ShellShebangException()
        self.eval()


def eval(self):
    pass


if __name__ == "__main__":
    bash_content = "!/bin/bash"
    try:
        shell_script = ShellScript(bash_content)
    except ShellEmptyException as e:
        print(e)
        print("Передайте не пустой файл скрипта")
    except ShellShebangException as e:
        print(e)
        print("Валидация на шебанг не пройдена")
