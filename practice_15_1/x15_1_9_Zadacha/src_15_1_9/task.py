import datetime


class Task:
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
        self.run_time = run_time

    # логические методы реализуются в начале класса
    def __str__(self):
        return f"{self.name}, Статус выполнения: {self.status}, Дата создания: {self.created_at}"

    def __add__(self, other):
        return self.run_time + other.run_time

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

    print(task.name)
    print(task.description)
    print(task.status)
    print(task.created_at)

    task2 = Task.new_task("Купить билеты", "Купить билеты на самолёт")

    print(task2.name)
    print(task2.description)
    print(task2.status)
    print(task2.created_at)

    task2.created_at = "29.05.2026"
    print(task2.created_at)
    task2.created_at = "29.06.2026"
    print(task2.created_at)

    print(task + task2)