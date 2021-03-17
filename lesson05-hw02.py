"""2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке."""

my_file = open("lesson05-hw02.txt", "r", encoding='utf-8')
i = 1
for line in my_file:
    my_list = [line.split()]
    print(f"Строка {i} состоит из  {len(my_list)} слов")
    i += 1
print(f"Всего в файле {i} строк.")
my_file.close()
