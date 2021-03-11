"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль"""


def division_int(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return


int_one = int(input("Введите первое число:"))
int_two = int(input("Введите второе число:"))

print(division_int(int_one, int_two))
