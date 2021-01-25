'''Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток,
соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n*****.'''


class Cell:
    def __init__(self, numbers_cell):
        self.view = []
        self.numbers = numbers_cell

    def __add__(self, other):
        self.numbers = self.numbers + other.numbers
        return self

    def __sub__(self, other):
        if (self.numbers - other.numbers) < 0:
            return 'Нельзя выполнить эту операцию'
        else:
            self.numbers = self.numbers - other.numbers
            return self

    def __mul__(self, other):
        self.numbers = self.numbers * other.numbers
        return self

    def __truediv__(self, other):
        self.numbers = int(self.numbers / other.numbers)
        return self

    def __str__(self):
        self.view.clear()
        for count in range(self.numbers):
            self.view.append('*')
        return ''.join(self.view)

    def make_order(self, cell_in_row):
        for count in range(self.numbers // cell_in_row):
            print(''.join(self.view[:cell_in_row]) + '\n')
        return (''.join(self.view[:(self.numbers % cell_in_row)]) +
                ('\n' if (self.numbers % cell_in_row) != 0 else ''))


cell_1 = Cell(20)
cell_2 = Cell(10)
cell_3 = Cell(12)
print(f'Cell -1 {cell_1}')
print(f'Cell -2 {cell_2}')
print(f'Cell -3 {cell_3}')
print(f'Cell - 1 по рядам')
print(cell_1.make_order(7))
print(f'Cell - 2 по рядам')
print(cell_2.make_order(3))
print(f'Cell - 3 по рядам')
print(cell_3.make_order(5))
print(f'Cell 1 + 2 {cell_1 + cell_2}')
print(f'Cell - 1 по рядам')
print(cell_1.make_order(7))
print(f'Cell 2 - 3 {cell_2 - cell_3}')
print(f'Cell - 2 по рядам')
print(cell_2.make_order(3))
print(f'Cell 2 * 3 {cell_2 * cell_3}')
print(f'Cell - 2 по рядам')
print(cell_2.make_order(10))
print(f'Cell - 3 по рядам')
print(cell_3.make_order(10))
print(f'Cell 2 / 3 {cell_2 / cell_3}')
print(f'Cell - 2 по рядам')
print(cell_2.make_order(10))
