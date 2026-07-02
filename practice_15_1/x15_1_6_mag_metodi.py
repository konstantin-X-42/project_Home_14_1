class BigFuncClass:

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def __repr__(self):
        return f'{self.__class__.__name__}({self.attr1}, {self.attr2})'

    def __str__(self):
        return f'{self.attr1} - {self.attr2}'

    def __len__(self):
        return len(f'{self.attr1}{self.attr2}')

    def __add__(self, other):
        self.attr1 += other.attr1
        self.attr2 += other.attr2

    def __call__(self, *args, **kwargs):
        print(f'Был вызван объект {self}')

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        if self.current_value + 1 < len(self):
            self.current_value += 1
            return str(self)[self.current_value]
        else:
            raise StopIteration

    def __enter__(self):
        self.fp = open(self.attr1, self.attr2)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()

bfc1 = BigFuncClass('1', '2')
bfc2 = BigFuncClass('3', '4')

# -------------------------------------------------------
# Запустить визуализацию выполнения этого Python-кода, лучше всего использовать бесплатный интерактивный
# инструмент Python Tutor. Он пошагово показывает, как создаются объекты в памяти,
# как меняются атрибуты класса и куда ведут ссылки на переменные.
# https://pythontutor.com/
# -------------------------------------------------------


# Исправленный пример для демонстрации контекстного менеджера
# и всех остальных методов класса
bfc1 = BigFuncClass('test.txt', 'w')
bfc2 = BigFuncClass('3', '4')

# 1. Проверка __add__
bfc1 + bfc2

# =================================
# 2. Проверка __str__ и __repr__
print("\n- - Проверка __str__ и __repr__ - -")
# =================================
print(str(bfc1))
print(repr(bfc1))

# =================================
# 3. Проверка __len__
print("\n- - Проверка __len__ - -")
# =================================
print(len(bfc1))

# 4. Проверка __call__
bfc1()

# =================================
# 5. Проверка __iter__ и __next__
print("\n- - Проверка __iter__ и __next__ - -")
# =================================
for char in bfc2:
    print(char)

# 6. Проверка __enter__ и __exit__
with BigFuncClass('demo_15_1_6.txt', 'w') as f:
    f.write('Hello!')