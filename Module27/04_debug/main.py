from typing import Any, Callable
import functools


def debug(func: Callable) -> Callable:
    """ Декоратор, вызывающий имя функции и что возвращает"""
    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        print("Вызывается {}({})".format(
            func.__name__,
            ", ".join(
                list(f"\"{arg}\""
                     if isinstance(arg, str) else
                     str(arg) for arg in args)
                +
                list(f"{k}=\"{v}\""
                     if isinstance(v, str) else
                     f"{k}={v}" for k, v in kwargs.items())
            )
        ))
        print("'{}' вернула значение'{}'".format(
            func.__name__, result
        ))
        print(result)
        return result

    return wrapped



@debug
def greeting(name, age=None):
    """Функция возвращающая строку"""
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)



greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)