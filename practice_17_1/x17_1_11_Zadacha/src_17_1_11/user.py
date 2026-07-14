"""
Задачи "Исключения"
1. Если пользователь создает задачу с отрицательным временем выполнения, вызвать исключение ValueError.
Переопределить сообщение при выбрасывании ошибки - Задачу с отрицательным временем выполнения создать нельзя.
2. В классе User реализовать новый метод, который будет подсчитывать среднее время выполнения задач пользователя.
С помощью исключений обработать случай, когда у пользователя нет задач. В случае если такое происходит, возвращайте ноль.
3. Создать класс исключение, который будет обрабатывать случай добавления пользователю задачи с нулевым
временем выполнения и выводить соответствующее сообщение. При этом, важно в случае успешного добавления задачи,
вывести сообщение о том, что задача добавлена. И также при любом исходе вывести сообщение,
что обработка добавления задачи завершена.
4. Написать тесты для нового функционала
"""

from practice_17_1.x17_1_11_Zadacha.src_17_1_11.exceptions import ZeroRunTimeTask
from practice_17_1.x17_1_11_Zadacha.src_17_1_11.task import Task

# ================================
# запуск тестов с покрытием во всех модулях
# poetry run pytest practice_17_1/x17_1_11_Zadacha/tests_17_1_11 --cov=practice_17_1/x17_1_11_Zadacha/src_17_1_11 --cov-report=term-missing
# ================================


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
        return (
            f"{self.last_name} {self.first_name}, Email: {self.email}, Всего задач в списке: {len(self.__task_list)}"
        )

    @property
    def task_list(self):
        task_str = ""
        for task in self.__task_list:
            task_str += f"{str(task)}\n"
        return task_str

    @task_list.setter
    def task_list(self, task: Task):
        """Добавление листа __task_list и увеличение значения задач"""
        if isinstance(task, Task):  # проверка, что передаются только экземпляры класса Task
            try:
                if task.run_time == 0:
                    raise ZeroRunTimeTask("Нельзя задать задачу с нулевым временем выполнения")
            except ZeroRunTimeTask as e:
                print(str(e))
            else:  # если ошибки не возникает, в блоке происходит добавление задач пользователя и увеличение счётчика
                self.__task_list.append(task)
                User.all_tasks_count += 1
                print("Задача добавлена успешно")
            finally:  # выполняется после выполнения try (с else) или except
                print("Обработка выполнения задачи завершена")
        else:
            raise TypeError  # если атрибут иного класса - возбуждаем ошибку

    @property
    def task_in_list(self):
        return self.__task_list

    # ===================================
    # 17.1 метод для пользователя вычисляет среднее время выполнения его задач
    def middle_task_runtime(self):
        try:
            return sum([task.run_time for task in self.__task_list]) / len(self.__task_list)
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":
    task1 = Task("Купить огурцы", "Купить огурцы для салата", run_time=20)
    task2 = Task("Купить помидоры", "Купить помидоры для салата", run_time=20)
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

    # задача с нулевым временем выполнения
    # task5 = Task("Купить огурцы", "Купить огурцы для салата")
    # user.task_list = task5

    print(user.task_list)  # >>> Купить огурцы, Статус выполнения: Ожидает старта, Дата создания: 08.07.2026
    print(User.all_tasks_count)  # >>> 5

    print(user)  # >>> Userov User, Email: user@mail.ru, Всего задач в списке: 5

    # проверяем среднее время работы программы у пользователей
    print(user.middle_task_runtime())  # >>> 8.0

    # проверяем среднее время работы программы без задач у пользователей
    user1 = User("User", "user@mail.ru", "User", "Userov", [])
    print(user1.middle_task_runtime())  # >>> 0

    # задача с назначенным временем выполнения
    task5 = Task("Купить огурцы", "Купить огурцы для салата", run_time=60)
    user.task_list = task5
