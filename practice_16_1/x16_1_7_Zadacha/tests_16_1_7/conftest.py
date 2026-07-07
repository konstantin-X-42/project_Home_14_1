# import pytest
# from task import Task
# from user import User
# from  task_iterator import TaskIterator

import pytest
from practice_16_1.x16_1_7_Zadacha.src_16_1_7.task import Task
from practice_16_1.x16_1_7_Zadacha.src_16_1_7.user import User
from practice_16_1.x16_1_7_Zadacha.src_16_1_7.task_iterator import TaskIterator

# from src_16_1_7.task import Task
# from src_16_1_7.user import User


# @pytest.fixture — это декоратор, превращает функцию в изолированный тестовый объект
@pytest.fixture
def first_user():
    return User(
        username="User",
        email="user@mail.ru",
        first_name="User",
        last_name="Userov",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата", created_at="02.07.2026"),
            Task("Купить помидоры", "Купить помидоры для салата", created_at="02.07.2026"),
        ],
    )


# 1. Декоратор, который регистрирует функцию ниже как фикстуру Pytest
@pytest.fixture
def second_user():
    # 2. Создаем и возвращаем объект класса User, заполняя его атрибуты
    return User(
        username="John",
        email="john@mail.ru",
        first_name="John",
        last_name="Doe",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата", created_at="02.07.2026"),
            Task("Купить помидоры", "Купить помидоры для салата", created_at="02.07.2026"),
            Task("Купить лук", "Купить лук для салата", created_at="02.07.2026"),
        ],
    )


# фикстура задач


@pytest.fixture
def task():
    return Task("Купить огурцы", "Купить огурцы для салата", created_at="12.06.2026")


@pytest.fixture
def task_with_runtime1():
    return Task("Купить помидоры", "Купить помидоры для салата", created_at="12.06.2026", run_time=60)


@pytest.fixture
def task_with_runtime2():
    return Task("Купить перец", "Купить перец для салата", created_at="12.06.2026", run_time=70)


@pytest.fixture
def task_iterator(second_user):
    return TaskIterator(second_user)
