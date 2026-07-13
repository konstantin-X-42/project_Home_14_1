"""
Задачи "Множественное наследование"
1. Создайте базовый абстрактный класс с именем BaseTask, выделите общий функционал, 
который должен быть у каждой задачи и опишите его в абстрактном классе. 
Включите абстрактный класс в существующую цепочку наследования классов.
2.Реализуйте класс-миксин для классов задач различных типов, который будет при создании объекта, 
автоматически печатать в консоль информацию о том, от какого класса и с какими параметрами был создан объект.
Например:
Task('Задача1', 'Описание задачи', 'Ожидает старта', '02.04.2024')
3.Напишите тесты для нового функционала
"""

from practice_17_1.x17_1_11_Zadacha.src_17_1_11.task import Task


# from task import Task
# from .task import Task
# from practice_15_1.x15_1_9_Zadacha.src_17_1_11.task import Task
# from src_17_1_11.task import Task


class User:
    username: str
    email: str
    first_name: str
    task_list: list
    users_count = 0
    all_tasks_count = 0

    def __init__(self, username, email, first_name, last_name, task_list=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.__task_list = task_list if task_list else []
        User.users_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0

    def __str__(self):
        return f'{self.last_name} {self.first_name}, Email: {self.email}, Всего задач в списке: {len(self.__task_list)}'

    @property
    def task_list(self):
        task_str = ""
        for task in self.__task_list:
            task_str += f"{str(task)}\n"
        return task_str

    @task_list.setter
    def task_list(self, task: Task):
        """ Добавление листа __task_list и увеличение значения задач"""
        if isinstance(task, Task):  # проверка, что передаются только экземпляры класса Task
            self.__task_list.append(task)
            User.all_tasks_count += 1
        else:
            raise TypeError  # если атрибут иного класса - возбуждаем ошибку

    @property
    def task_in_list(self):
        return self.__task_list


if __name__ == "__main__":
    task1 = Task("Купить огурцы", "Купить огурцы для салата")
    task2 = Task("Купить помидоры", "Купить помидоры для салата")
    task3 = Task("Купить лук", "Купить лук для салата")
    task4 = Task("Купить перец", "Купить перец для салата")

    user = User("User", "user@mail.ru", "User", "Userov", [task1, task2, task3, task4])

    print(user.username)
    print(user.email)  # >>> 1
    print(user.first_name)  # >>> 4
    print(user.last_name)  # >>> Купить огурцы, Статус выполнения: Ожидает старта, Дата создания: 08.07.2026
    print(user.task_list)  # >>> Купить помидоры, Статус выполнения: Ожидает старта, Дата создания: 08.07.2026

    print(user.users_count)  # >>> Купить лук, Статус выполнения: Ожидает старта, Дата создания: 08.07.2026
    print(User.all_tasks_count)  # >>> Купить перец, Статус выполнения: Ожидает старта, Дата создания: 08.07.2026

    task5 = Task("Купить огурцы", "Купить огурцы для салата")
    user.task_list = task5

    print(user.task_list)  # >>> Купить огурцы, Статус выполнения: Ожидает старта, Дата создания: 08.07.2026
    print(User.all_tasks_count)  # >>> 5

    print(user)  # >>> Userov User, Email: user@mail.ru, Всего задач в списке: 5
