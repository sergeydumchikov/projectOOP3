from abc import ABC
import math

class Figure(ABC):
    """Абстрактный базовый класс фигура"""
    def __init__(self, lenght_a: int) -> None:
        self.__lenght_a = lenght_a

    @property
    def lenght(self) -> int:
        return self.__lenght_a

    def squre(self) -> int:
        return self.__lenght_a ** 2

    def perimetr(self) -> int:
        return self.__lenght_a * 4



class Triangle(Figure):
    """Дочерний класс Треугольник"""
    def __init__(self, lenght_a: int, height: int) -> None:
        super().__init__(lenght_a)
        self.__height = height

    def squre(self) -> float:
        return (self.lenght / 2) * self.__height

    def perimetr(self) -> float:
        return self.lenght + 2 * math.sqrt((self.lenght/2)**2 + self.__height**2)


    @property
    def height(self) -> int:
        return self.__height

class Quadrate(Figure):
    """
    Дочерний класс Квадрат
    """

class Cub(Quadrate):
    """Дочерний класс Куб"""

    def squre_Cub(self) -> int:
        return self.squre() * 6


class Pir(Triangle):
    """Дочерний класс Пирамида"""

    def squre_pir(self) -> float:
        return self.squre() * 4 + self.lenght**2


cub = Cub(lenght_a=10)
pir = Pir(lenght_a=10, height=15)

quer = Quadrate(10)
print(quer.squre())
print(quer.perimetr())
print(cub.squre_Cub())

tria = Triangle(10, 15)
print(tria.squre())
print(tria.perimetr())
print(pir.squre_pir())