from src_14_2_8.user import User

# from practice_14_2.x14_2_8_Zadacha.src_14_2_8.user import User

# from ..src_14_2_8.user import User

# ================================
# установка покрытия тестами
# poetry add pytest-cov --group dev
# ================================
# запуск тестов
# poetry run pytest practice_14_2/x14_2_8_Zadacha/tests_14_2_8/test_user.py
# ================================
# запуск тестов с покрытием
# poetry run pytest SkyPro_14_1_9_Zadachya/tests/test_user.py --cov=SkyPro_14_1_9_Zadachya/src
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
        "Купить огурцы, Статус выполнения: Ожидает старта, Дата создания: 21.06.2026\n"
        "Купить помидоры, Статус выполнения: Ожидает старта, Дата создания: 21.06.2026\n"
    )


def test_user_task_setter(first_user, task):
    assert len(first_user.task_in_list) == 2
    first_user.task_list = task
    assert len(first_user.task_in_list) == 3
