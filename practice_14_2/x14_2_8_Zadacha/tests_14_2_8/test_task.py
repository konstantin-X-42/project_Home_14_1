# ================================
# запуск тестов
# poetry run pytest SkyPro_14_1_9_Zadachya/tests/test_task.py
# ================================


def test_task_init(task):
    assert task.name == "Купить огурцы"
    assert task.description == "Купить огурцы для салата"
    assert task.status == "Ожидает старта"
    assert task.created_at == "12.06.2026"
