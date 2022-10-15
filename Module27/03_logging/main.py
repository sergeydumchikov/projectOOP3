from typing import Callable
import datetime



def logging(func: Callable) -> Callable:
    print('Вызываемая функция: {name}\nДокументация: {doc}'.format(name=func.__name__, doc=func.__doc__))
    for i in func():
        try:
            if not i.isalpha():
                raise TypeError
        except TypeError as e:
            with open('function_errors.log', mode='a') as file:
                print('{date} {name} TypeError\n'.format(date=datetime.datetime.now(), name=func.__name__), e, file=file)
    return func


@logging
def names() -> list:
    """Функция список имен
     :return Список"""
    name_list = ['Sergey1', 'Petr21', 'Sveta', 'Anrey89']
    return name_list



my_names = names()

