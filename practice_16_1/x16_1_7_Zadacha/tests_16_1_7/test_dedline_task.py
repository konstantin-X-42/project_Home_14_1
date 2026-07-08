import pytest

def test_dedline_task(task_deadline1):
    """ Проверяем инициализацию """
    assert task_periodic1.name == 'Купить огурцы'
    assert task_periodic1.description == 'Купить огурцы для салата'
    assert task_periodic1.start_data == '01.01.2026'
    assert task_periodic1.end_data == '01.01.2026'
    assert task_periodic1.status == 'Ожидает старта'
    assert task_periodic1.created_at == '12.06.2026'
    assert task_periodic1.frequency == 'Ежедневная'