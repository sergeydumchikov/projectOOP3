from typing import Callable
from time import sleep


def timer(func: Callable) -> Callable:
    sleep(3)
    return func


@timer
def hello():
    print('Hello')


hello()