from math import cos
from math import sin

class Automobile:
    """
    Базовый класс описывающий текущие координаты и направление движения

    """
    def __init__(self, x, y, fi):
        """
        Инициализация параметров
            fi (int) = направление
        """
        self.x = x
        self.y = y
        self.fi = fi

    def __str__(self):
        """
        :return: Вывод информации на экран
        """
        return f'x = {self.x}\ny = {self.y}\nfi = {self.fi}'

    def move(self, dist):
        """
       Движение автомобиля в соответствии с направлении
        """
        self.x = self.x + dist * cos(self.fi/180)
        self.y = self.y + dist * sin(self.fi/180)


class Bus(Automobile):
    """
    Дочерний класс описывающий движение автобуса
        pay (int) = стоимость проезда
        max_pas (int) = вместимость автобуса
        passegers (int) = текущее кол-во пассажиров
        money (int) = сколько денег собрал водитель
    """
    pay = 0.01
    max_pas = 60

    def __init__(self, x, y, direction):
        """
        Инициализация параметров

        """
        super().__init__(x, y, direction)
        self.passengers = 0
        self.money = 0

    def move(self, distance):
        """
        Движение автобуса в соответствии с направлением
        """
        self.money += self.pay * self.passengers * distance
        super().move(distance)

    def enter(self, passengers):
        """
      Вход пассажиров
        """
        if passengers + self.passengers > self.max_pas:
            print('Достигнута максимальная вместимость автобуса')
            print('Уехать смогли только {:d}'.format(self.max_pas - self.passengers))
            print('Остались {:d}'.format(passengers - (self.max_pas - self.passengers)))
            passengers = self.max_pas - self.passengers
        return passengers

    def exit(self, passengers):
        """
        Выход пассажиров
        :return:
        """
        if passengers > self.passengers:
            print('Вышли все из автобуса')
            passengers = self.passengers
        return passengers

    def __str__(self):
        lines = [
            super().__str__(),
            f'В автобусе {self.passengers} пассажиров',
            f'У водителя {round(self.money, 2)} денег',
        ]
        return '\n'.join(lines)


auto = Automobile(0, 0, 90)
auto.move(1)
print(auto)

bus = Bus(0, 0, 30)
print(bus)