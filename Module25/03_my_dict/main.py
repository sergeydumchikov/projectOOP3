class Mydict(type):
    """
    Базовый класс описывающий аналог словаря
    Args:
        *args = позиционные арг-ты
        **kwargs = непозиционные арг-ты
        mydict (dict) = словарь
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализация входных данных
        :param args: ключ
        :param kwargs: значение
        """
        super().__init__(*args, **kwargs)
        self.mydict = {}

    def __delitem__(self, key):
        """
        Позволяет задать поведение при попытке удаления элемента контейнера

        """
        del self.mydict[key]

    def __setitem__(self, key, value):
        """
        Позволяет задать поведение при инициализации элемента контейнера значением.

        """
        self.mydict[key] = value

    def __getitem__(self, key):
        """
        Позволяет задать поведение при обращении к элементу контейнера.

        """
        return self.mydict[key]

    def clear(self):
        self.mydict.clear()

    def pop(self, *args, **kwargs):
        return self.mydict.pop(*args, **kwargs)

    def popitem(self):
        return self.mydict.popitem()

    def setdefault(self, *args, **kwargs):
        return self.mydict.setdefault(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.mydict.update(*args, **kwargs)

    def __contains__(self, key):
        return key in self.mydict

    def get(self, *args, **kwargs):
        if self.mydict.get(*args, **kwargs) == None:
            return 0
        else:
            return self.mydict.get(*args, **kwargs)



    def items(self):
        return self.mydict.items()

    def keys(self):
        return self.mydict.keys()

    def values(self):
        return self.mydict.values()

    def __len__(self):
        return len(self.mydict)

    def __iter__(self):
        return iter(self.mydict)

class Adict(metaclass=Mydict):
    pass

Adict['key'] = 'value'
print(dict(Adict)) # {'key': 'value'}
print({**Adict, 'key2': 'value2'}) # {'key': 'value', 'key2': 'value2'}
print(Adict.get(7))
