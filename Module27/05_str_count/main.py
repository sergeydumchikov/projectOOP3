from typing import Callable, Any

def counter(func: Callable) -> Callable:
    """Декоратор считающий кол-во вызовов функции"""
    def wrapped(*args, **kwargs) -> Any:
        wrapped.count += 1
        res = func(*args, **kwargs)
        print('Функция {fun} была вызвана {cou} раз'.format(fun=func.__name__, cou=wrapped.count))
        return res

    wrapped.count = 0
    return wrapped

@counter
def hello():
    print('Hello')

hello()
hello()
hello()
hello()