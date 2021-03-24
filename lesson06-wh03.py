"""Реализовать базовый класс Worker (работник).

определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
        print("Worker")
        print(self._income)


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super(Position, self).__init__(name, surname, position, income)
        self.get_full_name = str(self.name) + " " + str(self.surname)
        self.get_total_income = sum(self._income.values())
        print("Position")
        print(f"Полное имя сотрудника: {self.get_full_name} и его доход: {self.get_total_income}")


incom_dict = {"wage": 10000, "bonus": 2500}
Position("Tom", "Jons", "enginer", incom_dict)
