import pytest

from practice_17_1.x17_1_11_Zadacha.src_17_1_11.user import User
from practice_17_1.x17_1_11_Zadacha.src_17_1_11.task import Task


# ================================
# установка покрытия тестами
# poetry add pytest-cov --group dev
# ================================
# запуск тестов в модуле test_user
# poetry run pytest practice_17_1/x17_1_11_Zadacha/tests_17_1_11/test_user.py
# ================================
# запуск тестов с покрытием в модуле test_user
# poetry run pytest practice_17_1/x17_1_11_Zadacha/tests_17_1_11/test_user.py --cov=practice_17_1/x17_1_11_Zadacha/src_17_1_11 --cov-report=term-missing
# ================================
# запуск тестов с покрытием во всех модулях
# poetry run pytest practice_17_1/x17_1_11_Zadacha/tests_17_1_11 --cov=practice_17_1/x17_1_11_Zadacha/src_17_1_11 --cov-report=term-missing
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


def test_middle_runtime(first_user, user_without_tasks):
    """ тест на вычисление среднего времени выполнения задач пользователя"""
    assert first_user.middle_task_runtime() == 45
    """ тест на вычисление среднего времени выполнения без задач пользователя"""
    assert user_without_tasks.middle_task_runtime() == 0


def test_custom_exception(capsys, first_user):
    """ тест работы с кастамной (написаной самим) ошибкой, capsys - перехватывает поток вывода"""
    assert  len(first_user.task_in_list) == 2

    task_add1 = Task("Купить огурцы", "Купить огурцы для салата", created_at="02.07.2026")
    """ создаём задачу будем добавлять пользователю"""
    first_user.task_list = task_add1
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-2] == "Нельзя задать задачу с нулевым временем выполнения" # [-2] берем предпоследнее сообщение

    task_add = Task("Купить огурцы", "Купить огурцы для салата", created_at="02.07.2026", run_time=60)
    """ создаём задачу будем добавлять пользователю"""
    first_user.task_list = task_add
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-2] == "Задача добавлена успешно" # [-2] берем предпоследнее сообщение
    assert message.out.strip().split('\n')[-1] == "Обработка выполнения задачи завершена" # [-1] берем последнее сообщение