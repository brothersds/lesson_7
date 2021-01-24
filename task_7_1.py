'''Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.'''

import random


class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def array(self, rows, cols):
        return [[random.randint(-10, 10) for _ in range(rows)] for _ in range(cols)]

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.list_of_lists])

    def __add__(self, other):
        for line in range(len(self.list_of_lists)):
            for index in range(len(self.list_of_lists[0])):
                self.list_of_lists[line][index] = self.list_of_lists[line][index] + other.list_of_lists[line][index]
        return self


mat1 = Matrix(Matrix.array(1, 5, 5))
mat2 = Matrix(Matrix.array(2, 5, 5))
mat3 = Matrix(Matrix.array(3, 5, 5))
mat123 = mat1 + mat2 + mat3
print(f'Первая матрица: \n{mat1}\n')
print(f'Вторая матрица: \n{mat2}\n')
print(f'Третья матрица: \n{mat3}\n')
print(f'Общая матрица:  \n{mat123}\n')
