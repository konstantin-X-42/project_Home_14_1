import datetime

from practice_17_1.x17_1_11_Zadacha.src_17_1_11.base_task import BaseTask
from practice_17_1.x17_1_11_Zadacha.src_17_1_11.print_mixin import PrintMixin


class Task(BaseTask, PrintMixin):
    name: str
    description: str
    status: str
    created_at: str
    run_time: int

    def __init__(self, name, description, status="Ожидает старта", created_at=None, run_time=0):
        self.name = name
        self.description = description
        self.status = status
        self.__created_at = created_at or datetime.date.today().strftime("%d.%m.%Y")
        if run_time >= 0:
            self.run_time = run_time
        else:
            raise ValueError("Задачу с отрицательным временем выполнения создать нельзя")
        super().__init__()

    # логические методы реализуются в начале класса
    def __str__(self):
        return f"{self.name}, Статус выполнения: {self.status}, Дата создания: {self.created_at}"

    def __add__(self, other):
        if type(other) is Task:  # проверка, что передаются только экземпляры класса Task
            return self.run_time + other.run_time
        raise TypeError  # если атрибут иного класса - возбуждаем ошибку

    @classmethod
    def new_task(cls, name, description, status="Ожидает старта", created_at=None):
        return cls(name, description, status, created_at)

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, new_date: str):
        new_dt = datetime.datetime.strptime(new_date, "%d.%m.%Y").date()
        old_dt = datetime.datetime.strptime(self.__created_at, "%d.%m.%Y").date()

        if new_dt < old_dt:
            print("Нельзя изменить дату создания на дату из прошлого")
            return

        self.__created_at = new_date


if __name__ == "__main__":
    task = Task("Купить огурцы", "Купить огурцы для салата", run_time=60)

    print(task.name)  # >>> Купить огурцы
    print(task.description)  # >>> Купить огурцы для салата
    print(task.status)  # >>> Ожидает старта
    print(task.created_at)  # >>> 11.07.2026

    task2 = Task.new_task("Купить билеты", "Купить билеты на самолёт")

    print(task2.name)  # >>> Купить билеты
    print(task2.description)  # >>> Купить билеты на самолёт
    print(task2.status)  # >>> Ожидает старта
    print(task2.created_at)  # >>> 11.07.2026

    task2.created_at = "29.05.2026"  # >>> Нельзя изменить дату создания на дату из прошлого
    print(task2.created_at)  # >>> 11.07.2026
    task2.created_at = "29.06.2026"  # >>> Нельзя изменить дату создания на дату из прошлого
    print(task2.created_at)  # >>> 11.07.2026

    # ==============================================
    # проверяем правильность обработки соответствия атрибутов текущему классу
    # ==============================================
    print(task + task2)  # >>> 60
    # task + 5               # >>> ошибка raise TypeError - если атрибут иного класса - возбуждаем ошибку

# ==============================================
# проверяем задачу с отрицательным временем иполнения
# ==============================================
# task = Task("Купить огурцы", "Купить огурцы для салата", run_time=-60)
