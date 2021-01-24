'''Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        print('Расход ткани: ')
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 38:
            self._size = 38
        elif size > 74:
            self._size = 74
        else:
            self._size = size

    @abstractmethod
    def consumption(self, size):
        print('Расчет расхода ткани')


class Coat(Clothes):
    def consumption(self, size):
        return (size / 6.5) + 0.5


class Suit(Clothes):
    def consumption(self, size):
        return 2 * size + 0.5


coat1 = Coat.consumption(1, 45)
coat2 = Coat.consumption(2, 30)
suit1 = Suit.consumption(1, 50)
suit2 = Suit.consumption(2, 80)
consumption = round((coat1 + coat2 + suit1 + suit2), 2)
print(f'Общий расход ткани = {consumption} погонных метра')
