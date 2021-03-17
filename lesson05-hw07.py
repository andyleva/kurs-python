"""7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать .
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
Подсказка: использовать менеджер контекста."""

import json

my_file = open("text_7.txt", "r", encoding='utf-8')
"""Словарь с прибылью"""
my_dict_profit = {}
"""Словарь с убытком"""
my_dict_lesion = {}
sum_profit = 0
count_profit = 0

for line in my_file:
    my_list = (line.split())
    """расчет прибыли/убытка"""
    profit = int(my_list[2]) - int(my_list[3])
    """назхначение ключа словаря"""
    my_key = str(my_list[0] + " " + my_list[1])
    """распределение по словарям прибылей и убытков"""
    my_dict_profit[my_key] = profit

    """сложение и среднее по прибыли"""
    if profit > 0:
        sum_profit += profit
        count_profit += 1

avg_profit = int(sum_profit / count_profit)
list_profit = [my_dict_profit, {"average_profit": avg_profit}]
print(list_profit)

"""преобразование json"""
print("Формат python:")
with open("text_77.json", "w", encoding='utf-8') as write_file:
    json.dump(list_profit, write_file, indent=4, ensure_ascii=False, separators=(',', ':'))

    print("Формат json:")
    print(json.dumps(list_profit, indent=4, ensure_ascii=False, separators=(',', ':')))
