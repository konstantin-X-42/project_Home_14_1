class ZeroRunTimeTask(Exception):
    """ Кастомская ошибка возбуждается если пользователю добавляется задача с нулевым временем """
    def __init__(self, message=None):
        super().__init__(message)