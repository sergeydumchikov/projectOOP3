def gen_lists(lst2: list, lst1: list, find: int):
    for x in lst1:
        yield x
        for y in lst2:
            yield y
            result = x * y
            print(x, y, result)
            if result == find:
                print('Found!!!')
                return


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

for y in gen_lists(list_2, list_1, to_find):
    pass