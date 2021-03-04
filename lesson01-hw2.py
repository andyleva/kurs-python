2.  # Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
sec_int = int(input("введите время в секундах:"))
second_int = sec_int % 60
hour_int = sec_int // 60 // 60
minute_int = sec_int // 60 - hour_int * 60
print(f"{hour_int:02d}" + ":" + f"{minute_int:02d}" + ":" + f"{second_int:02d}")
