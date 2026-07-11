from practice_16_2.x16_2_7_Zadacha.src_16_2_7.task import Task
from practice_16_2.x16_2_7_Zadacha.src_16_2_7.periodic_task import PeriodicTask
from practice_16_2.x16_2_7_Zadacha.src_16_2_7.dedline_task import DeadlineTask

# ================================
# Запускаем print(message)
# pytest -s
# ================================
# ================================
# запуск тестов
# poetry run pytest practice_16_2/x16_2_7_Zadacha/tests_16_2_7/test_print_mixin.py
# ================================

def test_print_mixin(capsys):  # вывод в консоль используем capsys
    Task("Купить огурцы", "Купить огурцы для салата", created_at="12.06.2026")
    message = capsys.readouterr()
    # print(message)
    assert message.out.strip() == "Task(Купить огурцы, Купить огурцы для салата, Ожидает старта, 12.06.2026)"

    PeriodicTask("Купить огурцы",
                        "Купить огурцы для салата",
                        "01.01.2026",
                        "01.01.2026",
                        run_time=60,
                        created_at="12.06.2026")
    message = capsys.readouterr()
    # print(message.out.strip())
    assert message.out.strip() == "PeriodicTask(Купить огурцы, Купить огурцы для салата, Ожидает старта, 12.06.2026)"

    DeadlineTask("Купить перец",
                            "Купить перец для салата",
                            "15.07.2026",
                            run_time=60,
                            created_at="12.06.2026")
    message = capsys.readouterr()
    # print(message.out.strip())
    assert message.out.strip() == "DeadlineTask(Купить перец, Купить перец для салата, Ожидает старта, 12.06.2026)"

