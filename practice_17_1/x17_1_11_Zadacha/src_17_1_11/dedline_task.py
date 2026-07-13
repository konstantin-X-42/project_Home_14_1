from practice_17_1.x17_1_11_Zadacha.src_17_1_11.task import Task

class DeadlineTask(Task):
    """ Класс отвечает за задачу конечного срока (deadline) """
    def __init__(self,
                 name,
                 description,
                 deadline,
                 status="Ожидает старта",
                 created_at=None,
                 run_time=0): # задаём инициализацию

        super().__init__(name, description, status, created_at, run_time)
        self.deadline = deadline


    def __add__(self, other):
        if type(other) is DeadlineTask:   # проверка, что передаются только экземпляры класса DeadlineTask
            return self.run_time + other.run_time
        raise TypeError  # если атрибут иного класса - возбуждаем ошибку


if __name__ == "__main__":
    deadline_task = DeadlineTask("Купить огурцы",
                                 "Купить огурцы для салата",
                                 "15.07.2026",
                                 run_time=60)

# ==============================================
# проверяем правильность вывода атрибутов класса
# ==============================================
    print(deadline_task.name)        # >>> Купить огурцы
    print(deadline_task.description) # >>> Купить огурцы для салата
    print(deadline_task.status)      # >>> Ожидает старта
    print(deadline_task.created_at)  # >>> 08.07.2026

    print(deadline_task.deadline)    # >>> 15.07.2026

# ==============================================
# проверяем правильность обработки соответствия атрибутов текущему классу
# ==============================================
    task = Task("Купить огурцы", "Купить огурцы для салата", run_time=60)
    # print(deadline_task + task)              # >>> raise TypeError - если атрибут иного класса - возбуждаем ошибку

