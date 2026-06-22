"""
Задачи"Режимы доступа"
1. Для класса User сделайте список задач приватным атрибутом, чтобы к нему нельзя было получить доступ вне класса.
2. Добавьте геттер для приватного атрибута списка задач.
   Геттер должен возвращать данные о каждой задаче в списке в формате:
    Название задачи, Статус выполнения: Ожидает старта, Дата создания: 01.04.2024
3. Для добавления задач пользователю реализуйте отдельный метод (сеттер) в классе User.
   При этом не забудьте увеличить счетчик задач всех пользователей.
4. Для класса Task реализуйте класс-метод, который будет принимать на вход параметры задачи и
   возвращать созданный объект класса Task.
5. Для класса Task сделайте атрибут даты создания приватным и опишите геттеры и сеттеры.
   В сеттере реализуйте проверку: в случае если дата создания раньше, чем сегодняшняя выводите сообщение в консоль
   "Нельзя изменить дату создания на дату из прошлого", при этом новую дату устанавливать не нужно.
6. Напишите тесты на новый функционал.
"""
from src_14_2_8.task import Task

# from .task import Task
# from practice_14_2.x14_2_8_Zadacha.src_14_2_8.task import Task
# from task import Task

class User:
    username: str
    email: str
    first_name: str
    task_list: list
    users_count = 0
    all_tasks_count = 0

    def __init__(self, username, email, first_name, last_name, task_list = None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.__task_list = task_list if task_list else []
        User.users_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0

    @property
    def task_list(self):
        task_str = ""
        for task in self.__task_list:
            task_str += f'{task.name}, Статус выполнения: {task.status}, Дата создания: {task.created_at}\n'
        return task_str

    @task_list.setter
    def task_list(self, task: Task):
        self.__task_list.append(task)
        User.all_tasks_count += 1

    @property
    def task_in_list(self):
        return self.__task_list


if __name__ == "__main__":
    task1 = Task("Купить огурцы", "Купить огурцы для салата")
    task2 = Task("Купить помидоры", "Купить помидоры для салата")
    task3 = Task("Купить лук", "Купить лук для салата")
    task4 = Task("Купить перец", "Купить перец для салата")

    user = User('User', 'user@mail.ru', 'User', 'Userov', [task1, task2, task3, task4])

    print(user.username)
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(user.task_list)

    print(user.users_count)
    print(User.all_tasks_count)

    task5 = Task("Купить огурцы", "Купить огурцы для салата")
    user.task_list = task5

    print(user.task_list)
    print(User.all_tasks_count)
