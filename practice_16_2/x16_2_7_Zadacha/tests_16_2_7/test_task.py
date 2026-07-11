import datetime
from practice_16_2.x16_2_7_Zadacha.src_16_2_7.task import Task

# from task import Task
# from src_16_2_7.task import Task

# ================================
# запуск тестов
# poetry run pytest practice_16_2/x16_2_7_Zadacha/tests_16_2_7/test_task.py
# ================================


def test_task_init(task):
    assert task.name == "Купить огурцы"
    assert task.description == "Купить огурцы для салата"
    assert task.status == "Ожидает старта"
    assert task.created_at == "12.06.2026"


def test_task_create():
    task = Task("Купить билеты", "Купить билеты на самолёт")
    task.name = "Купить билеты"
    task.description = "Купить билеты на самолёт"
    task.status = "Ожидает старта"
    task.created_at = datetime.datetime.now().date().strftime("%d.%m.%Y")


def test_task_update(capsys, task):
    task.created_at = "29.06.2025"
    message = capsys.readouterr()
    # split("\n")[-1] - разрезает текст на список строк везде, где встречается перенос строки (\n),
    # [-1] - берет самый последний элемент из этого списка (то есть последнюю строку)
    assert message.out.strip().split("\n")[-1] == "Нельзя изменить дату создания на дату из прошлого"

    task.created_at = datetime.datetime.now().date().strftime("%d.%m.%Y")
    assert task.created_at == datetime.datetime.now().date().strftime("%d.%m.%Y")


# тесты на строковое представление
def test_task_str(task):
    assert str(task) == "Купить огурцы, Статус выполнения: Ожидает старта, Дата создания: 12.06.2026"

# тест на проверку сложения экземпляров класса
def test_task_add(task_with_runtime1, task_with_runtime2):
    assert task_with_runtime1 + task_with_runtime2 == 130
