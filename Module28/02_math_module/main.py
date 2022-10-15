import math
from abc import ABC


class MyMath(ABC):
    """Абстрактный класс MyMath"""

    @classmethod
    def circle_len(cls, radius: int) -> float:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        return math.pi * radius ** 2

    @classmethod
    def cube_value(cls, edge: int) -> float:
        return edge ** 3

    @classmethod
    def sphere_area(cls, radius: int) -> float:
        return 4 * math.pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)