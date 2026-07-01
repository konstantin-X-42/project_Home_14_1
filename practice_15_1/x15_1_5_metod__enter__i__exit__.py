class MyOpen:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.fp = open(self.filename, self.mode)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()

# применение
with MyOpen('text.txt', 'r') as fp: # Открываем файл
    print(fp.read()) # Читаем файл