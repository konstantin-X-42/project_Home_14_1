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