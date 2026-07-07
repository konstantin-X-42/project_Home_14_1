"""
Задачи"Магические методы"
1. Для класса Task добавить строковое отображение в следующем виде:
Название задачи, Статус выполнения: Ожидает старта, Дата создания: 01.04.2024
В геттере списка задач в классе User используйте строковое представление для задачи

2. Для класса User добавить строковое отображение в следующем виде:
Фамилия имя, Email: example@example.com, Всего задач в списке: 5

3. Для класса Task добавьте новое поле - плановое время выполнения в минутах.
Реализуйте логику сложения экземпляров класса Task. Результатом сложения будет
суммарная длительность выполнения задач в минутах (целым числом)

4. Создайте новый вспомогательный класс, с помощью которого можно перебирать задачи одного пользователя,
например, в цикле for. Для этого новый класс должен принимать на вход объект класса User и производить
итерацию по задачам, которые есть у данного пользователя.
То есть метод выполнения следующего шага итерации должен возвращать очередную задачу из списка задач пользователя.

5. Напишите тесты на новый функционал
"""

from practice_16_1.x16_1_7_Zadacha.src_16_1_7.task import Task
# from task import Task
# from .task import Task
# from practice_15_1.x15_1_9_Zadacha.src_16_1_7.task import Task
# from src_16_1_7.task import Task


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

    user = User("User", "user@mail.ru", "User", "Userov", [task1, task2, task3, task4])

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

    print(user)