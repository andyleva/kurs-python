"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл."""

my_file = open("lesson05-hw04.txt", "r", encoding='utf-8')
"""объявлен пустой словарь"""

my_list_new = []
for line in my_file:
    # print(line)
    list_split = list(line.split())
    for item in list_split:
        if list_split[0] == "One":
            list_split[0] = "Один"
        elif list_split[0] == "Two":
            list_split[0] = "Два"
        elif list_split[0] == "Three":
            list_split[0] = "Три"
        elif list_split[0] == "Four":
            list_split[0] = "Четыре"

    my_list_new.append(list_split)
my_file.close()

# print(my_list_new)

my_file_new = open("lesson05-hw04-new.txt", "w", encoding='utf-8')

for el in my_list_new:
    # print(el)
    str_el = (" ".join(el))
    my_file_new.write(str_el + '\n')

my_file_new.close()

print("END PROGRAMM")
