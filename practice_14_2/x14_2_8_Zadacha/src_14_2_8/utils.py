import json
import os  # библиотека для взаимодействия с операционной системой ПК

from task import Task
from user import User


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(
        full_path, "r", encoding="UTF8"
    ) as file:  # открываем файл по указанному пути
        data = json.load(file)  # чтение файла
        return data


# ================================
print("\n--  --  read_json()  --  --\n")
# ================================

if __name__ == "__main__":
    # Находим абсолютный путь к data.json динамически, чтобы не ломались тесты
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_dir, "..", "data", "data.json")
    raw_data = read_json(full_path)
    print(raw_data)


# >>> [{'username': 'alex', 'email': 'alex@gmail.com', 'first_name': 'Alex', 'last_name': 'Tomas',
# 'task_list': [{'name': 'Купить батон', 'description': 'Купить батон когда будешь в магазине',
# 'created_at': '01.02.2024'}, {'name': 'Поиграть с собакой',
# 'description': 'Взять собаку и поехать к озеру поиграть и погулять', 'status': 'Выполнено',
# 'created_at': '13.02.2024'}, {'name': 'Встретиться с друзьями',
# 'description': 'Забронировать ресторан на 15.02 на встречу с 5 друзьями', 'status': 'Выполнено',
# 'created_at': '15.02.2024'}]}, {'username': 'john', 'email': 'john@gmail.com', 'first_name': 'John',
# 'last_name': 'Borg', 'task_list': [{'name': 'Сдать сессию',
# 'description': 'Сдать все экзамены до 15.02', 'created_at': '01.02.2024'}]}]


def create_objects_from_json(data):
    """функция будет создавать объекты из полученных данных"""

    # список будет заполняться экземплярами класса user
    users = []
    for user in data:
        tasks = []
        for task in user["task_list"]:
            tasks.append(Task(**task))
        user["task_list"] = tasks
        users.append(User(**user))
    return users


# ================================
print("\n--  --  create_objects_from_json()  --  --\n")
# ================================

if __name__ == "__main__":

    # Находим абсолютный путь к data.json динамически, чтобы не ломались тесты
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_dir, "..", "data", "data.json")

    # 1. читаем данные из файла в переменную raw_data
    raw_data = read_json(full_path)

    # 2. Передаем эти данные в функцию создания объектов
    users_data = create_objects_from_json(raw_data)

    #  список, содержащий созданные объекты класса User
    print(users_data)
    # Имя первого пользователя
    print(users_data[0].username)
    # Список задач из json файла привязанных к первому пользователю, состоящий из реальных объектов класса
    print(users_data[0].task_list)


# >>> [<src.user.User object at 0x00000168DBDF9FD0>, <src.user.User object at 0x00000168DBDFE350>]
# >>> alex
# >>> [<src.task.Task object at 0x00000168DBDFA270>, <src.task.Task object at 0x00000168DBDFD1D0>,
# <src.task.Task object at 0x00000168DBDFD310>]
