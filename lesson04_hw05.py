"""5. Реализовать формирование списка, используя функцию range() и возможности генератора. В
список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить
результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce() ."""

from functools import reduce


def my_func(arg1, arg2):
    return arg1 * arg2


my_list = range(100, 1001)
print(list(my_list))
new_list = list(el for el in my_list if el % 2 == 0)
print(new_list)
print(reduce(my_func, new_list))
