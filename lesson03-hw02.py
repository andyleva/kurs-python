"""2. Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Осуществить вывод данных о
пользователе одной строкой."""


def parameters(def_name, def_surname, def_year, def_email, def_telefone, def_city):
    print(def_name, def_surname, def_year, def_city, def_email, def_telefone)


name = input("Введите свое имя:")
surname = input("Введите свою фамилию:")
year = input("Введите год рождения:")
city = input("Введите город проживания:")
email = input("Введите свой email:")
telefone = input("Введите свой телефон:")

parameters(def_name=name, def_surname=surname, def_year=year, def_city=city, def_email=email, def_telefone=telefone)
