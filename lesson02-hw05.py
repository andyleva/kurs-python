# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
# не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
my_list = [8, 5, 4, 4, 2, 1, 1]
z = 0
while z!=3:
    int_input = int(input("Введите натуральное число:"))
    if (int_input in my_list):
        ind = my_list.index(int_input)  # определение номера индекса/позиции в list
        cnt = my_list.count(int_input)  # определение количества одниковых позиции в list
        my_list.insert(ind + cnt - 1, int_input)  # добавление в список
        print(my_list)

        # for i in my_list:
        #    if i == int_input:
        # print(int_input)

    else:  # Элемента в списке нет
        # поиск элементов рядом в большую сторону
        result = any(ele > int_input for ele in my_list)
        if result == True:
            element_find = False
            i = 0
            while element_find == False:  # поиск элемента рядом в большую сторону
                i += 1
                element_find = int_input + i in my_list  # поиск элемента # any(ele == int_input + i for ele in my_list)

                if element_find == True:
                    element_find_index = my_list.index(int_input + i)
                    cnt = my_list.count(int_input + i)  # определение количества одниковых позиции в list
                    my_list.insert(element_find_index + i + cnt - 1, int_input)  # добавление в список
                    print(my_list)
        else:  # поиск элемента рядом в меньшую сторону если не нашли в большую сторону
            element_find = False
            i = 0
            while element_find == False:
                i += 1
                element_find = int_input - i in my_list
                if element_find == True:
                    element_find_index = my_list.index(int_input - i)  # поиск элемента
                    cnt = my_list.count(int_input - i)  # определение количества одниковых позиции в list
                    my_list.insert(element_find_index, int_input)  # добавление в список
                    print(my_list)
    z+=1 #три варианта ввода