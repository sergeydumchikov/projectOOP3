from typing import Callable
import functools

def decorator_with_args_for_any_decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapped


@decorator_with_args_for_any_decorator
def decorated_decorator(*args, **kwargs):
    def decor(func: Callable) -> Callable:
        print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapped
    return decor



@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print(f'Hello, {text} {num}')

decorated_function('User', 101)