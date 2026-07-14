import pytest

from practice_17_1.x17_1_11_Zadacha.src_17_1_11.dedline_task import DeadlineTask
from practice_17_1.x17_1_11_Zadacha.src_17_1_11.periodic_task import PeriodicTask
from practice_17_1.x17_1_11_Zadacha.src_17_1_11.task import Task
from practice_17_1.x17_1_11_Zadacha.src_17_1_11.task_iterator import TaskIterator
from practice_17_1.x17_1_11_Zadacha.src_17_1_11.user import User


# @pytest.fixture — это декоратор, превращает функцию в изолированный тестовый объект
@pytest.fixture
def first_user():
    return User(
        username="User",
        email="user@mail.ru",
        first_name="User",
        last_name="Userov",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата", created_at="02.07.2026", run_time=60),
            Task("Купить помидоры", "Купить помидоры для салата", created_at="02.07.2026", run_time=30),
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
    return Task("Купить огурцы", "Купить огурцы для салата", created_at="12.06.2026", run_time=60)


@pytest.fixture
def task_with_runtime1():
    return Task("Купить помидоры", "Купить помидоры для салата", created_at="12.06.2026", run_time=60)


@pytest.fixture
def task_with_runtime2():
    return Task("Купить перец", "Купить перец для салата", created_at="12.06.2026", run_time=70)


@pytest.fixture
def task_iterator(second_user):
    return TaskIterator(second_user)


@pytest.fixture
def task_periodic1():
    return PeriodicTask(
        "Купить огурцы", "Купить огурцы для салата", "01.01.2026", "01.01.2026", run_time=60, created_at="12.06.2026"
    )


@pytest.fixture
def task_periodic2():
    return PeriodicTask(
        "Купить помидоры",
        "Купить помидоры для салата",
        "01.01.2026",
        "01.01.2026",
        run_time=60,
        created_at="12.06.2026",
    )


@pytest.fixture
def task_deadline1():
    return DeadlineTask("Купить перец", "Купить перец для салата", "15.07.2026", run_time=60, created_at="12.06.2026")


@pytest.fixture
def task_deadline2():
    return DeadlineTask("Купить лук", "Купить лук для салата", "15.07.2026", run_time=60, created_at="12.06.2026")


@pytest.fixture
def user_without_tasks():
    """Содержание пользователя без задач"""
    return User(
        username="Some",
        email="some@mail.ru",
        first_name="Some",
        last_name="User",
    )
