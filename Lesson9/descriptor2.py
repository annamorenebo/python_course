class SrtType:

    def __set__(self, instance, value):
        if type(value) == int:
            raise TypeError('Значение должно быть в формате строки')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = SrtType()
    surname = SrtType()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


worker_data = [
    Worker(1, 'Иванов', 'Директор', 100000, 10000),
    Worker('Петр', 'Петров', 'Бухгалтер', 90000, 5000),
    Worker('Сергей', 'Сергеев', 'Курьер', 30000, 2000)
]
