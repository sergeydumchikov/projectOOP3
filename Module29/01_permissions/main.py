import functools
from typing import Callable

def check_permission(name: str) -> Callable:
    user_permissions = ['admin']
    def check_decor(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Callable:
            try:
                if name in user_permissions:
                    return func(*args, **kwargs)
                else:
                    raise Exception
            except Exception:
                print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {func_name}'.format(
                func_name=func.__name__))

        return wrapped
    return check_decor



@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('frog')
def add_comment():
    print('Добавляем комментарий')



delete_site()
add_comment()