
class MyIterator:
    """
    Базовый класс описывающий итератор
        Args:
            __limit(int) = максимальное значение
            __counter (int) = счетчик конца
            __num (int) = возвращаемое число
    """
    def __init__(self, limit: int) -> None:
        """
        Инициализация аргументов
        """
        self.__limit = limit
        self.__counter = 0
        self.__num = 0

    def __iter__(self):
        """

        :return: Итератор
        """
        return self

    def __next__(self) -> int:
        self.__num += 1
        self.__counter += 1
        if self.__counter > 1:
            if self.__counter > self.__limit:
                raise StopIteration

        return self.__num**2

my_inter = MyIterator(limit=10)
for i in my_inter:
    print(i)

def generator(limit):
    for num in range(limit):
        yield num**2

for i in generator(10):
    print(i)

nums = (num**2 for num in range(10))
for i in nums:
    print(i)