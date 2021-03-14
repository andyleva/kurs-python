"""Реализовать функцию int_func() , принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’))  -> Text.
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
        if ord(item) > 122 or ord(item) < 97 or item.isupper():
            flag_ascii = False
            break
    return flag_ascii


txt = input("Введите маленькие латынские буквы в виде одного слова:")
"""проверка на маленькие латинские буквы"""
result_ascii_test = ascii_test(txt)
if result_ascii_test != False:
    print(int_func(txt))
else:
    print("Вы не выполнили условие ввода слова! Программа завершена.")
