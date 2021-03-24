"""2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property."""

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):

    @abstractmethod
    def growth(self):
        # """расчет расхода для пальто"""
        pass

    @abstractmethod
    def size(self):
        # """расчет расхода для костюма"""
        pass


class Expense(MyAbstractClass):
    def __init__(self, v, h):
        self.h = h
        self.v = v

    def growth(self):
        self.expense = self.v / 6.5 + 0.5
        return (self.expense)

    def size(self):
        self.expense = 2 * self.h + 0.3
        return (self.expense)

    @property
    def my_growth_size(self):
        self.expense_all = self.v / 6.5 + 0.5 + 2 * self.h + 0.3
        return self.expense_all


my_expense = Expense(52, 190)
print(f"расчет расхода для костюма {my_expense.size()}")
print(f"расчет расхода для пальто: {my_expense.growth()}")
print(f"расчет общего расхода: {my_expense.growth() + my_expense.size()}")


print("Применение @property:")
my_expense.v = 60
my_expense.h = 170
print(f"расчет общего расхода: {my_expense.my_growth_size:9.2f}")

my_expense.v = 46
my_expense.h = 175
print(f"расчет общего расхода: {my_expense.my_growth_size:9.2f}")