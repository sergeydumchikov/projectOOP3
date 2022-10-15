class Person():
    """
    Базовый класс описывающий проживающиего в доме
        Args:
            __name (str) = имя проживающего
            home (dict) = словарь
            satiety (int) = степень сытости
            numeat (int) = количество съеденой еды

    """
    def __init__(self, name, home):
        """

        Инициализация аргументов
        """
        self.__name = name
        self.home = home
        self.satiety = 30
        self.numeat = 0

    def eat(self):
        """
        Метод описывающий прием пищи
        meal (int) = количество еды принимаемой за раз
        """
        meal = 30
        self.satiety += meal
        self.home['Eat'] -= meal
        self.numeat += 30

    def get_num_eat(self):
        """

        :return: общее кол-во съеденой еды
        """
        return self.numeat

    def set_to_satiety(self):
        """
        Проверка сытости

        """
        if self.satiety <= 20:
            self.eat()




class Hus(Person):
    """
    Дочерний класс описывающий действия мужа проживающего в доме
        Args:
            __happiness (int) = степень счастья
    """
    def __init__(self, name, home):
        """
        Инициализация аргументов
        """
        super().__init__(name, home)
        self.__happiness = 100

    def work(self):
        """
        Метод описывающий работу мужа

        """
        self.satiety -= 10
        self.home['Money'] += 150

    def play(self):
        """
        Метод описывающий игру в компьютерные игры
        """
        self.satiety -= 10
        self.__happiness += 20

    def pet_the_cat(self):
        """
        Метод описывающий то как гладят кота
        """
        self.__happiness += 5
        self.satiety -= 10

    def set_money(self):
        """
        Проверка на наличие денег
        """
        if self.home['Money'] < 350:
            self.work()

    def set_happiness(self):
        """
        Проверка на упадок счатья
        """
        if self.__happiness <= 20:
            self.play()
            self.pet_the_cat()

    def set_dir_hap(self):
        """
        Проверка на чистоту в доме
        """
        if self.home['Dirt'] >= 100:
            self.__happiness -= 10



class Wife(Person):
    """
    Дочерний класс описывающий действия жены
        Args:
            __happiness (int) = степень счастья
            __money (int) = кол-во потраченных денег
            __numcoat (int) = кол-во купленных шуб
    """

    def __init__(self, name, home):
        """
        Инициализация аргументов
        """
        super().__init__(name, home)
        self.__happiness = 100
        self.__money = 0
        self.__numcoat = 0


    def buy_eat(self):
        """
        Метод описывающий покупку еды
        """
        self.satiety -= 10
        self.home['Eat'] += 200
        self.home['Money'] -= 200
        self.__money += 200

    def buy_eat_cat(self):
        """
        Метод описывающий покупку еды для кота
        """
        self.home['Eat_cat'] += 100
        self.home['Money'] -= 100
        self.__money += 100
        self.satiety -= 10

    def set_eat_cat(self):
        """
        Проверка наличия еды у кота
        """
        if self.home['Eat_cat'] <= 30:
            self.buy_eat_cat()

    def set_eat(self):
        """
        Проверка наличия еды в холодильнике
        """
        if self.home['Eat'] <= 60:
            self.buy_eat()

    def buy_coat(self):
        """
        Метод описывающий покупку шубы
        """
        self.satiety -= 10
        self.__happiness += 60
        self.home['Money'] -= 350
        self.__money += 350
        self.__numcoat += 1

    def clearning(self):
        """
        Метод описывающий уборку в доме
        """
        self.satiety -= 10
        self.home['Dirt'] -= 50

    def set_to_dirt(self):
        """
        Проверка на загрязненность дома
        """
        if self.home['Dirt'] >= 150:
            self.clearning()
            self.satiety -= 10

    def pet_the_cat(self):
        """
       Метод описывающий то как гладят кота
        """
        self.__happiness += 5
        self.satiety -= 10

    def set_happiness(self):
        """
       Проверка на упадок счастья
        """
        if self.__happiness < 20:
            if self.__numcoat < 1:
                self.buy_coat()
            self.pet_the_cat()


    def get_money(self):
        """
        :return Общее кол-во потраченных денег
        """
        return self.__money

    def num_coat(self):
        """
        :return: кол-во купленных шуб
        """
        return self.__numcoat

    def set_dir_hap(self):
        """
        Метод описывающий упадок счастья из-за загрязненности
        """
        if self.home['Dirt'] >= 100:
            self.__happiness -= 10



class Pet(Person):
    """
    Дочерний класс описывающий действие кота
        Args:
            numeatcat (int) = кол-во съеденной еды котом
    """
    def __init__(self, name, home):
        """
        Инициализация аргументов
        """
        super().__init__(name, home)
        self.numeatcat = 0

    def eat(self):
        """
       Метод описывающий прием пищи кота
        """
        self.satiety += 20
        self.home['Eat_cat'] -= 10
        self.numeatcat += 10

    def set_eat_cat(self):
        """
        Проверка степени сытости
        """
        if self.satiety <= 20:
            self.eat()

    def sleep(self):
        """
        Сон
        """
        self.satiety -= 10

    def get_num_eat_cat(self):
        """
        :return: общее кол-во съеденной еды котом
        """
        return self.numeatcat

    def wallpaper(self):
        """
        Метод описывающий то как кот дерет обои
        """
        self.satiety -= 10
        self.home['Dirt'] += 5




my_home = {
            'Eat': 50,
            'Eat_cat': 30,
            'Money': 100,
            'Dirt': 0
            }
hus = Hus('Sergey', my_home)
wife = Wife('Sveta', my_home)
cat = Pet('Bursick', my_home)

for _ in range(365):
    wife.set_eat_cat()
    hus.set_dir_hap()
    wife.set_dir_hap()
    hus.set_to_satiety() #проверка на голод
    wife.set_to_satiety() #проверка на голод
    cat.set_eat_cat() #проверка на голод
    my_home['Dirt'] += 5 #увеличение загрязненности
    hus.set_money() #проверка на наличие денег
    hus.set_happiness() #проверка на счастье
    wife.set_to_dirt() #проверка на грязь
    wife.set_happiness() #проверка на счастье
    wife.set_eat() #проверка на количество еды
    cat.sleep() #спит кот
    cat.wallpaper() #кот дерет обои


print('\nИтоги года:\nПотрачено денег {mon}\nСъедено еды {eat}\nСъедено котом {eat_cat}\nКуплено шуб {coat}'.format(
    mon=wife.get_money(),
    eat=wife.get_num_eat() + hus.get_num_eat(),
    eat_cat=cat.get_num_eat_cat(),
    coat=wife.num_coat()
))

