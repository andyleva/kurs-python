"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
время выполнения расчёта для конкретных значений необходимо запускать скрипт с
параметрами."""

from sys import argv

script_name, script_prodaction, script_rate, script_premium = argv

print(f"Размер заработной платы: {int(script_prodaction) * int(script_rate) - int(script_premium)}")
