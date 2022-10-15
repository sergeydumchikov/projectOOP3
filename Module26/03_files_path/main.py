import os

def gen_files_path(mypath: str)-> str:
   """
   :param mypath: каталог указанный пользователем
   :return: путь к файлу
   """
   for root, dirs, files in os.walk(mypath):
      print(f'Содержимое директории {root}')
      for filename in files:
         yield filename
         print(f'    Путь к файлу {root}\\{filename}')
      print()


path = 'C:\\Users\\serge\\OneDrive\\Рабочий стол\\Dumchikov  1999-2022'
for i in gen_files_path(path):
   pass

