import pytest

# ================================
# запуск тестов
# poetry run pytest practice_17_1/x17_1_11_Zadacha/tests_17_1_11/test_deadline_task.py
# ================================

def test_deadline_task_init(task_deadline1):
    """ Проверяем инициализацию """
    assert task_deadline1.name == 'Купить перец'
    assert task_deadline1.description == 'Купить перец для салата'
    assert task_deadline1.status == 'Ожидает старта'
    assert task_deadline1.created_at == '12.06.2026'
    assert task_deadline1.deadline == '15.07.2026'


def test_deadline_test_add(task_deadline1, task_deadline2):
    """ Проверяем сложение экземпляров deadline """
    assert task_deadline1 + task_deadline2 == 120


def test_deadline_test_add_error(task_deadline1):
    """ Проверяем при сложении экземпляров класса deadline возбуждается ошибка TypeError """
    with pytest.raises(TypeError):
        result = task_deadline1 + 1
