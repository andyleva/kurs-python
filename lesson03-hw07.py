"""6. Реализовать функцию int_func() , принимающую слова из маленьких л
возвращающую их же, но с прописной первой буквой. Например, print(int_func("text"))->text
7. Продолжить работу над заданием. В программу должна попадать строка из слов,
разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно
сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию ​int_func() ​.
"""


# уставовка прописной первой буквы
def int_func(text_input):
    str_text_input = str(text_input)
    txt_title = str_text_input.title()
    return txt_title


# проверка на маленькие латинские буквы
def ascii_test(txt_test):
    flag_ascii = True
    for item in txt_test:
        dd = ord(item)

        if ord(item) > 122 or ord(item) < 97 or item.isupper():
            if ord(item) != 32:
                flag_ascii = False
                break
    return flag_ascii


txt = input("Введите маленькие латынские буквы:")
"""проверка на маленькие латинские буквы"""
result_ascii_test = ascii_test(txt)
if result_ascii_test != False:
    for item in txt.split(" "):
        print(int_func(item))
else:
    print("Вы не выполнили условие ввода слова! Программа завершена.")
