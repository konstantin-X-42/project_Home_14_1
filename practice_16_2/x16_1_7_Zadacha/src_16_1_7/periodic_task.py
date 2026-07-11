from practice_16_1.x16_1_7_Zadacha.src_16_1_7.task import Task

class PeriodicTask(Task):
    """ Класс периодической задачи """
    def __init__(self,
                 name,
                 description,
                 start_data,
                 end_data,
                 status="Ожидает старта",
                 created_at=None,
                 run_time=0,
                 frequency='Ежедневная'):

        super().__init__(name, description, status, created_at, run_time) # передаём из родительского класса
        self.start_data = start_data
        self.end_data = end_data
        self.frequency = frequency


    def __add__(self, other):
        if type(other) is PeriodicTask:   # проверка, что передаются только экземпляры класса PeriodicTask
            return self.run_time + other.run_time
        raise TypeError  # если атрибут иного класса - возбуждаем ошибку


if __name__ == "__main__":
    periodic_task = PeriodicTask("Купить огурцы",
                                 "Купить огурцы для салата",
                                 "01.01.2026",
                                 "01.01.2026",
                                 run_time=60)

# ==============================================
# проверяем правильность вывода атрибутов класса
# ==============================================
    print(periodic_task.name)        # >>> Купить огурцы
    print(periodic_task.description) # >>> Купить огурцы для салата
    print(periodic_task.status)      # >>> Ожидает старта
    print(periodic_task.created_at)  # >>> 08.07.2026

    print(periodic_task.start_data)  # >>> 01.01.2026
    print(periodic_task.end_data)    # >>> 01.01.2026
    print(periodic_task.frequency)   # >>> Ежедневная

# ==============================================
# проверяем правильность обработки соответствия атрибутов текущему классу
# ==============================================
    periodic_task2 = PeriodicTask("Купить огурцы",
                                 "Купить огурцы для салата",
                                 "01.01.2026",
                                 "01.01.2026",
                                 run_time=60)

    task = Task("Купить огурцы", "Купить огурцы для салата", run_time=60)

    print(periodic_task + periodic_task2)  # >>> 120
    # print(periodic_task + task)            # >>> raise TypeError - если атрибут иного класса - возбуждаем ошибку
