import pytest
from src_14_2_8.task import Task
from src_14_2_8.user import User


# @pytest.fixture — это декоратор, превращает функцию в изолированный тестовый объект
@pytest.fixture
def first_user():
    return User(
        username="User",
        email="user@mail.ru",
        first_name="User",
        last_name="Userov",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата"),
            Task("Купить помидоры", "Купить помидоры для салата"),
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
            Task("Купить огурцы", "Купить огурцы для салата"),
            Task("Купить помидоры", "Купить помидоры для салата"),
            Task("Купить лук", "Купить лук для салата"),
        ],
    )


# фикстура задач


@pytest.fixture
def task():
    return Task("Купить огурцы", "Купить огурцы для салата", created_at="12.06.2026")
