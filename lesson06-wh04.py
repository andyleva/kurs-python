"""Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
 и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""
import random


class Car:
    # атрибуты класса

    # конструктор
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police  # булево

    # методы класса
    def go(self):  # машина поехала
        print(f"Автомобиль {self.name} {self.color} поехал.")

    def stop(self):  # машина остановилась
        print(f"Автомобиль {self.name} {self.color} остановился.")

    def turn(self, direction):  # машина повернула
        print(f"Автомобиль {self.name} {self.color} повернул {direction}")

    def show_speed(self):  # текущая скоркость авто
        print(f"Автомобиль {self.name} {self.color} едет со скоростью {self.speed}")


# дочерние классы
class TownCar(Car):
    # переопределить show_speed
    def show_speed(self, speed_car):
        if speed_car > 60 and speed_car <= 100:
            print("У этой машины скорость выше 60 км.=> TownCar")


class SportCar(Car):
    def show_speed(self, speed_car):
        if speed_car > 100:
            print("У этой машины скорость выше 100 км. => SportCar")


class WorkCar(Car):
    # переопределить show_speed
    def show_speed(self, speed_car):
        if speed_car > 40 and speed_car <= 60:
            print("У этой машины скорость выше 40 км.=> WorkCar")


class PoliceCar(Car):
    def show_police(self, police_car):
        if police_car == True:
            print("Это полицейская машина.")


"""Класс получение случайных аргументов из выборки"""


class Random_arg:
    def __init__(self):
        item = random.randint(0, 3)
        random_speed = [35, 39, 79, 10, 102]
        self.random_speed_el = random_speed[item]

        item = random.randint(0, 3)
        random_color = ["red", "white", "black", "blue", "yellow"]
        self.random_color_el = random_color[item]

        item = random.randint(0, 3)
        random_name = ["bmw", "mercedes", "bugatti", "kia", "lada"]
        self.random_name_el = random_name[item]

        item = random.randint(0, 3)
        random_go = ["стоит", "едет", "налево", "направо"]
        self.random_go_el = random_go[item]

        item = random.randint(0, 1)
        if item == 0:
            self.random_police_el = False
        else:
            self.random_police_el = True


# экземпляры класса

"""получение аргументов для выполнения задачи"""
my_arg = Random_arg()
speed_el = my_arg.random_speed_el
color_el = my_arg.random_color_el
name_el = my_arg.random_name_el
police_el = my_arg.random_police_el
go_el = my_arg.random_go_el

print(
    f"Аргументы задачи: Машина: {name_el} {color_el}, полицейская?: {police_el}, состояние: {go_el} со скоростью {speed_el}")
print("выполнение задачи:")

my_car = Car(speed_el, color_el, name_el, police_el)
if go_el == "едет":
    my_car.go()
elif go_el == "стоит":
    my_car.stop()
else:
    my_car.turn(go_el)

my_car.show_speed()

my_towncar = TownCar(speed_el, color_el, name_el, police_el)
my_towncar.show_speed(speed_el)

my_sportcar = SportCar(speed_el, color_el, name_el, police_el)
my_sportcar.show_speed(speed_el)

my_workcar = WorkCar(speed_el, color_el, name_el, police_el)
my_workcar.show_speed(speed_el)

my_policecar = PoliceCar(speed_el, color_el, name_el, police_el)
my_policecar.show_police(police_el)