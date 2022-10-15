from abc import ABC

class Konvertation(ABC):
    """Абстрактный базовый класс Конвертатор"""
    def __init__(self, date: str) -> None:
        self.__date = date
        self.list_date = self.__date.split('-')

    @property
    def date_s(self) -> str:
        return self.__date


class Date(Konvertation):
    """Дочерний класс Дата"""
    def __str__(self) -> str:
        return 'День: {day}     Месяц: {month}     Год: {year}'.format(
            day=self.list_date[0],
            month=self.list_date[1],
            year=self.list_date[2]
        )

    def date(self, date: str) -> None:
        if not isinstance(self.date, str):
            raise TypeError
        if self.list_date[0] not in range(1, 31) or self.list_date[1] not in range(1, 13) or len(
                self.list_date[2]) != 4:
            print('Ошибка ввода данных')
            raise Exception

    def is_date_valid(self, strin: str) -> True or False:
        if strin == self.date_s:
            return True
        else:
            return False



date = Date('10-12-2077')
print(date)
print(date.is_date_valid('10-12-2077'))
print(date.is_date_valid('40-12-2077'))