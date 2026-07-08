import pytest
from practice_16_1.x16_1_7_Zadacha.tests_16_1_7.conftest import task_periodic1


def test_periodic_task_init(task_periodic1):
    assert task_periodic1.name == 'Купить огурцы'
    assert task_periodic1.description == 'Купить огурцы для салата'
    assert task_periodic1.start_data == '01.01.2026'
    assert task_periodic1.end_data == '01.01.2026'
    assert task_periodic1.status == 'Ожидает старта'
    assert task_periodic1.created_at == '12.06.2026'
    assert task_periodic1.frequency == 'Ежедневная'

def test_periodic_task_add(task_periodic1, task_periodic2):
    """ Проверяем что сложение происходит успешно"""
    assert task_periodic1 + task_periodic2 == 120

def test_periodic_task_add_error(task_periodic1, task_periodic2):
    """ Проверяем что сложение происходит с ошибкой"""
    # result = task_periodic1 + 1   # проверяем в не контекстного менеджера возбуждается ошибка
    with pytest.raises(TypeError):
        result = task_periodic1 + 1