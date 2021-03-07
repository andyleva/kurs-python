# 3 Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому  времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict
#
# через List ************************************************************
month_list = ['Зима', 'Весна', 'Лето', 'Осень']
month_input_list = int(input("Проверка решения через LIST. Введите номер месяца от 1 до 12:"))
if month_input_list == 1 or month_input_list == 2 or month_input_list == 12:
    print(month_list[0])
elif month_input_list == 3 or month_input_list == 4 or month_input_list == 5:
    print(month_list[1])
elif month_input_list == 6 or month_input_list == 7 or month_input_list == 8:
    print(month_list[2])
elif month_input_list == 9 or month_input_list == 10 or month_input_list == 11:
    print(month_list[3])
elif month_input_list > 12:
    print(f"Вы ввели неправильниый номер месяца : {month_input_list}  программа завершена LIST!")
elif month_input_list <1:
    print(f"Вы ввели неправильниый номер месяца : {month_input_list}  программа завершена LIST!")

# через dict ************************************************************
month_dict = {"Зима": [1, 2, 12], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
month_input = int(input("Проверка решения через DICT. Введите номер месяца от 1 до 12:"))
if month_input > 12 or month_input < 1:
    print(f"Вы ввели неправильниый номер месяца: {month_input}  программа завершена DICT!")
else:
    for key in month_dict.keys():
        if month_input in month_dict[key]:
            print(key)
