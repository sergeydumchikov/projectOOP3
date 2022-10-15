import re
def gen(lst):
    for i in lst:
        yield i

mylist = ['9999999999', '999999-999', '99999x9999']

for i_srt in gen(mylist):
    if re.findall(r'\b[89]\d{9}', i_srt):
        print('Все в порядке')
    else:
        print('Не подходит')





