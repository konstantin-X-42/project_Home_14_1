from practice_17_1.x17_1_11_Zadacha.src_17_1_11.dedline_task import DeadlineTask
from practice_17_1.x17_1_11_Zadacha.src_17_1_11.periodic_task import PeriodicTask
from practice_17_1.x17_1_11_Zadacha.src_17_1_11.task import Task

# ================================
# Запускаем print(message)
# pytest -s
# ================================
# запуск тестов в модуле test_print_mixin
# poetry run pytest practice_17_1/x17_1_11_Zadacha/tests_17_1_11/test_print_mixin.py
# ================================


def test_print_mixin(capsys):  # вывод в консоль используем capsys
    Task("Купить огурцы", "Купить огурцы для салата", created_at="12.06.2026")
    message = capsys.readouterr()
    # print(message)
    assert message.out.strip() == "Task(Купить огурцы, Купить огурцы для салата, Ожидает старта, 12.06.2026)"

    PeriodicTask(
        "Купить огурцы", "Купить огурцы для салата", "01.01.2026", "01.01.2026", run_time=60, created_at="12.06.2026"
    )
    message = capsys.readouterr()
    # print(message.out.strip())
    assert message.out.strip() == "PeriodicTask(Купить огурцы, Купить огурцы для салата, Ожидает старта, 12.06.2026)"

    DeadlineTask("Купить перец", "Купить перец для салата", "15.07.2026", run_time=60, created_at="12.06.2026")
    message = capsys.readouterr()
    # print(message.out.strip())
    assert message.out.strip() == "DeadlineTask(Купить перец, Купить перец для салата, Ожидает старта, 12.06.2026)"
