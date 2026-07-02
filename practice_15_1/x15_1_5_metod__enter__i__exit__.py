class MyOpen:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.fp = open(self.filename, self.mode, encoding='utf-8')
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()


# Автоматически создаем файл для теста
with open('text_15_1_5.txt', 'w', encoding='utf-8') as f:
    f.write('Ура, контекстный менеджер работает!')


# применение
with MyOpen('text_15_1_5.txt', 'r') as fp: # Открываем файл
    print(fp.read()) # Читаем файл