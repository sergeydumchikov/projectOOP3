from typing import Callable
import functools
from datetime import datetime
import time



def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f'Завершение {func.__name__} время работы функции: ', round(finish-start, 3))
        return result
    return wrapped



def log_methods(decorator: Callable, date: str) -> Callable:
    @functools.wraps(decorator)
    def decorate(cls):
        format = date
        for sym in date:
            if sym.isalpha():
                format = format.replace(sym, '%' + sym)
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                print('Запускается {cls}.{met}'.format(cls=cls.__name__, met=i_method))
                print(f'Дата и время запуска {datetime.now().strftime(format)}\n')
                cur_method = getattr(cls, i_method)
                decor_method = decorator(cur_method)
                setattr(cls, i_method, decor_method)
        return cls
    return decorate






@log_methods(timer, "b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods(timer, "b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
