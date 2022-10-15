import itertools

my_list = '0123456789'
password = '3257'

for i in itertools.permutations(my_list, 4):
    true_pass = ''.join(i)
    if true_pass == password:
        print('Пароль: ', true_pass)
