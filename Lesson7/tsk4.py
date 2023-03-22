"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31 22
37 43
51 86
3 5 32
2 4 6
-1 64 -8
3 5 8 3
8 3 7 1
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая
матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix_numbers):

        self._x = None
        for row in matrix_numbers:
            if self._x is None:
                self._x = len(row)
            else:
                if self._x != len(row):
                    raise ValueError("Входной массив состоит из строк разной длины")

        self._y = len(matrix_numbers)
        self._matrix = matrix_numbers

    def __str__(self):
        return "\n".join(["".join([f"{x : 5}" for x in row]) for row in self._matrix])

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Слагаемое - не матрица")

        if not (self._x == other._x and self._y == other._y):
            raise ValueError("Размерность слагаемых матриц отличается")

        return Matrix([
            [x + y for x, y in zip(a, b)] for a, b in zip(self._matrix, other._matrix)
        ])


m1 = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

m2 = Matrix([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
])

print(m1 + m2)
