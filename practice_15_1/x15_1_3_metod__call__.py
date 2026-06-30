"""
Задача
Сделать класс с экземплярами, содержащими символы, которые надо удалять из строки.
Эта строка должна передаваться в качестве аргумента экземпляру класса.

Флоу решения:
1. Создать класс
2. Реализовать метод __init__
3. Реализовать метод __call__
"""

class StripChars:

# 2. метод __init__
    def __init__(self, chars):
        self.chars = chars

# 3. метод __call__
    def __call__(self, *args, **kwargs):
        return args[0].strip(self.chars)

# -----------------------------------------------------------------
st1 = StripChars('?')  # обращаем без знака ?

res = st1('?Example?')
print(res)  # >>> Example

res = st1('!SomeExample!') # перезаписываем res, здесь по краям знаки !
print(res)  # >>> !SomeExample!