import datetime
from pyexpat.errors import messages

from black import assert_equivalent
from src_14_2_8.task import Task

# ================================
# запуск тестов
# poetry run pytest practice_14_2/x14_2_8_Zadacha/tests_14_2_8/test_task.py
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
    assert message.out.strip() == "Нельзя изменить дату создания на дату из прошлого"

    task.created_at = datetime.datetime.now().date().strftime("%d.%m.%Y")
    assert task.created_at == datetime.datetime.now().date().strftime("%d.%m.%Y")
