class EvenRange:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        self.current_value = -2
        return self

    def __next__(self):
        if self.current_value + 2 < self.stop:
            self.current_value += 2
            return self.current_value
        else:
            raise StopIteration

# применение
r = EvenRange(9)  # [0, 2, 4, 6, 8]


result = list(r)
print(result)  # >>> [0, 2, 4, 6, 8]

# -------------------------------------------------------------------------------
print("\n- - Задача - -")
"""
Задача
Написать класс, который для заданного положительного целого числа N возвращает
последовательность четных чисел от 0 до N, не включая N.

Флоу решения:
1. Создать класс
2. Реализовать метод __iter__
3. Реализовать метод __next__
"""

class EvenRange:

    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        self.current_value = -2
        return self

    def __next__(self):
        if self.current_value + 2 < self.stop:
            self.current_value += 2
            return self.current_value
        else:
            raise StopIteration


for i in EvenRange(7):  # next(iter_r)
    print(i)  # >>> 0
              # >>> 2
              # >>> 4
              # >>> 6
