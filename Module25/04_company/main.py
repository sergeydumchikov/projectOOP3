class Person:
    """
    Базовый класс описывающий личность работника
    Args:
        __name (str) = Имя
        __family (str) = фамилмя
        __age (int) = возраст
    """
    def __init__(self, name, family, age):
        """
        Инициализация параметров

        """
        self.__name = name
        self.__family = family
        self.__age = age

    def __str__(self):
        return f'\t{self.__name}\t {self.__family}\t {self.__age}\t'


class Employe(Person):
    """
    Дочерний класс от Person описывающий заработную плату работников
    """
    def salary(self):
        money = 13000
        return money


class Manager(Employe):
    pass


class Agent(Employe):
    """
    Дочерний класс от Employe описывающий особенности расчета зарплаты Агента
    volume_of_sales (int) = объем продаж
    """
    def __init__(self, name, family, age, volume_of_sales):
        super().__init__(name, family, age)
        self.volume_of_sales = volume_of_sales

    def salary(self):
        money = ((int(self.volume_of_sales)/100) * 5) + 5000
        return money


class Worker(Employe):
    """
    Дочерний класс от Employe описывающий особенности расчета зарплаты worker
    hours (int) = отработанные часы
    """
    def __init__(self, name, family, age, hours):
        super().__init__(name, family, age)
        self.hours = hours

    def salary(self):
        money = 100 * self.hours
        return money

print('\n\tNAME\t FAMILY\t AGE\tSALARY')
manager_1 = Manager(name='Sergey', family='Ivanov', age=28)
print(f'{manager_1}\t{manager_1.salary()}')
manager_2 = Manager(name='Victor', family='Petrov', age=48)
print(f'{manager_2}\t{manager_2.salary()}')
manager_3 = Manager(name='Peter', family='Putin', age=25)
print(f'{manager_3}\t{manager_3.salary()}')

agent_1 = Agent(name='Semen', family='Popk', age=32, volume_of_sales=30000)
print(f'{agent_1}\t{agent_1.salary()}')
agent_2 = Agent(name='Goga', family='Rasteg', age=42, volume_of_sales=50000)
print(f'{agent_2}\t{agent_2.salary()}')
agent_3 = Agent(name='Bobi', family='Bubnov', age=37, volume_of_sales=20000)
print(f'{agent_3}\t{agent_3.salary()}')

worker_1 = Worker(name='Kiril', family='Sedov', age=33, hours=100)
print(f'{worker_1}\t{worker_1.salary()}')
worker_2 = Worker(name='Kiril', family='Petrov', age=23, hours=145)
print(f'{worker_1}\t{worker_1.salary()}')
worker_1 = Worker(name='Venia', family='Pivas', age=27, hours=90)
print(f'{worker_1}\t{worker_1.salary()}')