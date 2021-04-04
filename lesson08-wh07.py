"""7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и
умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
 и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if self.b + other.b < 0:
            txt = "-"
        else:
            txt = "+"
        return f'Сумма равна: {self.a + other.a} {txt} {self.b + other.b} * j'

    def __mul__(self, other):
        if (self.a * other.b)+(self.b * other.a)<0:
            txt="-"
        else:
            txt="+"
        return f'Произведение равно: {self.a * other.a - (self.b * other.b)} {txt} {abs((self.a * other.b)+(self.b * other.a))} * j'


c_1 = ComplexNumber(4, -8)
c_2 = ComplexNumber(6, 11)
print(c_1 + c_2)
print(c_1 * c_2)