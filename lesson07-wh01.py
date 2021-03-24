"""1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, my_list):
        # self.matrix=my_list
        self.matrix_print = '\n'.join(['\t'.join([str(j) for j in i]) for i in my_list])
        List = []
        for i in my_list:
            List.append([j for j in i])
        self.matrix = List

    def __str__(self):
        return str(self.matrix_print)

    def __add__(self, other):
        matrix_row = len(self.matrix)
        matrix_column = len(other.matrix[0])
        for i in range(matrix_row):
            for j in range(matrix_column):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        Result = self.matrix

        return Matrix(Result)


list_matrix_1 = [[31, 22], [37, 43], [51, 86]]
list_matrix_2 = [[5, 32], [2, 6], [-1, -8]]

mc_1 = Matrix(list_matrix_1)
mc_2 = Matrix(list_matrix_2)

print(mc_1 + mc_2)

