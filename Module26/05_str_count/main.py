import os

def gen_files_path(mypath: str):
    """
    :param mypath: название каталога
    :return: путь к файлу
    """
    for root, dirs, files in os.walk(mypath):
        for filename in files:
            yield filename


def gen_python_files(my_file):
    """
    :param my_file: Путь к файлу типа .py
    :return: строка
    """
    for i in my_file:
        if i == '\n' or i.startswith('#'):
            continue
        yield i


count = 0
path = os.path.abspath(os.path.join('..', '..'))
for mystr in gen_files_path(path):
    if mystr.endswith('.py'):
        with open(mystr, 'r') as file:
            for elem in gen_python_files(file):
                count += 1

print(f'Общее кол-во строк: {count}')