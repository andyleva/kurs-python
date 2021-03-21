"""3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32"""

my_file = open("lesson05-hw03.txt", "r", encoding='utf-8')
"""объявлен пустой словарь"""
my_dict = {}
my_list = []

for line in my_file:
    # print(line)
    list_surname_number = list(line.split())
    list_surname_number[1] = float(list_surname_number[1])
    my_list.append(list_surname_number)

my_dict = dict(my_list)
my_file.close()

"""максимальная зарплата"""
max_val = max(my_dict.values())
max_dict = {k: v for k, v in my_dict.items() if v == max_val}
# print (max_dict)
"""Сумма всех зарплат"""
sum_val = sum(my_dict.values())

"""количество СОТРУДНИКОВ и средняя зарплата"""
len_val = len(my_dict.values())
print(f"Средний доход: {int(sum_val / len_val)}")

"""Список сотрудников у кого зп ниже 20000"""
final_dict = {k: v for k, v in my_dict.items() if v < 20000}
print("Список сотрудников с минимальным доходом:")
print(final_dict)
