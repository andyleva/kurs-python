"""5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
её на экран."""

import random

with open("lesson05-hw05.txt", "w+", encoding='utf-8') as file_obj:
    list_number = []

    for item in range(20):
        number = random.randint(0, 100)
        list_number.append(str(number))

    str_list_number = (" ".join(list_number))

    file_obj.write(str_list_number)

    print("Запись в файл произведена успешно!")
    print(str_list_number)

    """расчет суммы чисел"""

    file_obj.seek(0)

    my_list = []

    for line in file_obj:
        # print(line)
        my_list = list(line.split())

    i = 0
    for el in my_list:
        my_list[i] = int(el)
        i += 1

    print(f"Сумма всех чисел, записанных в яайл = {sum(my_list)}")
