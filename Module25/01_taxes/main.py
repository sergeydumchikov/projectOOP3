class Property:
    """
    Базовый класс описывающий имущество
    атрибуты:
        per_tax (int) - процент налога
        name (str) - тип имущества
    Args:
        worth (int) - стоимость имущества
    """
    per_tax = 0
    name = ''

    def __init__(self, worth):
        self.worth = worth

    def how_many(self, money):
        """
        Хватает ли на покупку с учетом налога и сколько не хватает
        money (int) - сколько денег у пользователя

        """
        duty = self.tax() + self.worth
        if money < duty:
            print('Нехватает {} на покупку {}'.format((duty - money), self.name))

        else:
            print('Вам хватает на покупку {} с учетом налога'.format(self.name))

    def tax(self):
        """
        :return затраты на налог:
        """
        tax = self.worth * self.per_tax
        return tax


class Apartment(Property):
    name = 'Квартира'
    per_tax = 1 / 1000


class Car(Property):
    name = 'Машина'
    per_tax = 1 / 200


class CountryHouse(Property):
    name = 'Дача'
    per_tax = 1 / 500


money = int(input('Введите количество ваших средств: '))
price = int(input('Введите стоимость имущества, которое хотите приобрести: '))
print('Ниже приведены налоги на соответствующее имущество:')
prop_1 = Apartment(price)
prop_2 = Car(price)
prop_3 = CountryHouse(price)
print(prop_1.name, prop_1.tax())
print(prop_2.name, prop_2.tax())
print(prop_3.name, prop_3.tax())
prop_1.how_many(money)
prop_2.how_many(money)
prop_3.how_many(money)