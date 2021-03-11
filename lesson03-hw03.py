"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов."""


def my_func(arg1, arg2, arg3):
    arg_max1 = max(arg1, arg2)
    arg_max2 = max(arg3, arg_max1)
    print(f"Сумма двух наибольших аргументов: {arg_max2 + arg_max1}")


input_arg1 = int(input("Введите первый аргумент:"))
input_arg2 = int(input("Введите второй аргумент:"))
input_arg3 = int(input("Введите третий аргумент:"))

my_func(input_arg1, input_arg2, input_arg3)
