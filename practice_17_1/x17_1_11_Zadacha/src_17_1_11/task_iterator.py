from practice_17_1.x17_1_11_Zadacha.src_17_1_11.task import Task
from practice_17_1.x17_1_11_Zadacha.src_17_1_11.user import User


class TaskIterator:
    def __init__(self, user_obj):
        self.user = user_obj
        self.index = 0

    # 1. магический метод __iter__
    def __iter__(self):
        self.index = 0
        return self

    # 2. магический метод __next__(возвращает следующий элемент последовательности
    # и проверка на остановку перебора последовательности возвращает StopIteration)
    def __next__(self):
        if self.index < len(self.user.task_in_list):
            task = self.user.task_in_list[self.index]
            self.index += 1
            return task
        # по окончанию списка возбуждаем ошибку StopIteration
        else:
            raise StopIteration


if __name__ == "__main__":
    task1 = Task(name="Купить огурцы", description="Купить огурцы для салата")
    task2 = Task(name="Купить помидоры", description="Купить помидоры для салата")
    task3 = Task(name="Купить лук", description="Купить лук для салата")
    task4 = Task(name="Купить перец", description="Купить перец для салата")

    user = User(
        username="User",
        email="user@mail.ru",
        first_name="User",
        last_name="Userov",
        task_list=[task1, task2, task3, task4],
    )

    iterator = TaskIterator(user)

    for task in iterator:
        print(task)
    print("- - - - - - - - - - - -")
    for task in iterator:
        print(task)
