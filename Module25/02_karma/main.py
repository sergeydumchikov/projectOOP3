from random import randint
from random import choice

class LifeStimulation:
    """
    Базовый класс описывающий симуляцию жизни
    Атрибуты:
        __count (int) = количество очков кармы
    """
    __count = 0

    def one_day(self):
        """
        Начисление очков кармы от 1 до 7, а также с вероятностью 1 к 10 вывод ошибок
            karm (int) = кол-во начисляемой кармы
        """
        self.karm = randint(1, 7)
        self.__count += self.karm
        self.exept()

    def exept(self):
        """

        :return True если не было ошибок:
        Иначе ошибки следующих видов:
            KillError
            DrunkError
            CarCrashError
            GluttonyError
            DepressionError
        """
        if randint(1, 10) != 1:
            return True
        else:
            error = choice(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError'])
            print(error)

    def get_count(self):
        return self.__count

person = LifeStimulation()

while True:
    person.one_day()
    if person.get_count() >= 500:
        print('Уровень кармы достиг {}'.format(person.get_count()))
        break
print(LifeStimulation.__doc__)