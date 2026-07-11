import pytest
from practice_16_2.x16_2_7_Zadacha.src_16_2_7.user import User

# from user import User
# from src_16_2_7.user import User


# ================================
# установка покрытия тестами
# poetry add pytest-cov --group dev
# ================================
# запуск тестов
# poetry run pytest practice_16_2/x16_2_7_Zadacha/tests_16_2_7/test_user.py
# ================================
# запуск тестов с покрытием
# poetry run pytest practice_16_2/x16_2_7_Zadacha/tests_16_2_7/test_user.py --cov=practice_16_2/x16_2_7_Zadacha/src_16_2_7 --cov-report=term-missing
# ================================


def test_user_init(first_user, second_user):
    assert first_user.username == "User"
    assert first_user.email == "user@mail.ru"
    assert len(first_user.task_in_list) == 2

    # Все три строки ниже будут равны 2, потому что users_count — это общий атрибут класса,
    # который делят между собой все созданные пользователи

    # Обращение через экземпляр (объект) первого пользователя
    assert first_user.users_count == 2

    # Обращение через экземпляр (объект) второго пользователя
    assert second_user.users_count == 2

    # Или обращение напрямую ЧЕРЕЗ КЛАСС User
    assert User.users_count == 2

    # проверка количества задач (2 - у одного пользователя и 3 у другого)
    assert first_user.all_tasks_count == 5
    assert second_user.all_tasks_count == 5


def test_user_task_list_property(first_user):
    assert first_user.task_list == (
        "Купить огурцы, Статус выполнения: Ожидает старта, Дата создания: 02.07.2026\n"
        "Купить помидоры, Статус выполнения: Ожидает старта, Дата создания: 02.07.2026\n"
    )


def test_user_task_setter(first_user, task):
    assert len(first_user.task_in_list) == 2
    first_user.task_list = task
    assert len(first_user.task_in_list) == 3


# тест работы строкового представления
def test_user_str(first_user):
    # print(first_user) # проверяем, верно исполняется
    assert str(first_user) == "Userov User, Email: user@mail.ru, Всего задач в списке: 2"

# тест работы итератора
def test_task_iterator(task_iterator):
    iter(task_iterator)
    assert task_iterator.index == 0
    assert next(task_iterator).name == "Купить огурцы"
    assert next(task_iterator).name == "Купить помидоры"
    assert next(task_iterator).name == "Купить лук"

    with pytest.raises(StopIteration):
        next(task_iterator)


def test_user_task_setter_error(first_user, task):
    """ проверяем что возбуждается ошибка при неверном количестве списка объектов"""
    # assert first_user.task_list = 1 # проверяем что возбуждается ошибка
    with pytest.raises(TypeError):
        first_user.task_list = 1


def test_user_task_list_setter_periodic_task(first_user, task_periodic1):
    first_user.task_list = task_periodic1
    # print(first_user.task_in_list[-1].name) == "Купить огурцы" # смотрим что возвращает последняя задача
    assert first_user.task_in_list[-1].name == "Купить огурцы"

