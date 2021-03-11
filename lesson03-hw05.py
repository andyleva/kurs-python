"""5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу."""


def sum_numbers(def_str_numbers):
    list_str_numbers = def_str_numbers.split(" ")
    # print(list_str_numbers)

    """поиск символов"""
    err_symbol = False
    for item in list_str_numbers:

        try:
            index_item = list_str_numbers.index(item)  # определение индекса в list
            # print (index_item)
            int_item = int(item)  # попытка проверки на число, если ошибка, то это спецсимвол
        except ValueError:
            cut_list_ctr_number = list_str_numbers[:index_item]  # создание нового списка из чисел до спецсимвола
            print(f"в строке чисел обнаружен символ '{item}' и будут использованы данные: {cut_list_ctr_number}")
            err_symbol = True
            break

    if err_symbol == False:
        list_int_numbers = [int(i) for i in list_str_numbers]  # создание нового списка из чисел
    else:
        list_int_numbers = [int(i) for i in cut_list_ctr_number]  # создание нового списка из чисел где был спецсимвол
    print(f"Справочно! в расчете будут использованы следующие числа: {list_int_numbers}")
    return sum(list_int_numbers)


"""--------------------------------------------------------------------------------------------"""
i = 1
sum_all = 0  # расчет общей суммы
"""три запроса на ввод"""
for i in range(3):
    str_numbers = input("Введите числа через пробел:")
    sum_list_number = sum_numbers(str_numbers)
    print(sum_list_number)
    sum_all += sum_list_number
i += 1
print(f"Общая сумма введенных чисел: {sum_all}")
