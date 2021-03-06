"""4. Программа принимает действительное положительное число x и целое отрицательное число
y . Выполните возведение числа x в степень y . Задание реализуйте в виде функции
my_func(x, y) . При решении задания нужно обойтись без встроенной функции возведения
числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла."""

"""Решение по первому варианту"""


def degree_number_variant1(x, y):
    print(f"Вариант 1: {x ** y}")


def degree_number_variant2(x, y):
    """для целых чисел X в степени минус Y это 1/X**Y=> 4**(-2) =>1/4**2 =>1/16"""
    s = 1
    for i in range(abs(y)):
        s *= 1 / x
    print(f"Вариант 2: {s}")


input_x = abs(float(input("Введите число Х в виде действительного положительного числа:")))
input_y = int(input("Введите степень Y в виде целого отрицательного числа:"))
if input_y < 0:
    degree_number_variant1(input_x, input_y)
    degree_number_variant2(input_x, input_y)
else:
    print("Неверно введено значение Y!")
