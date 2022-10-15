#1 способ
for i in range(1001):
    print(i)

#2
def gen_print(num):
    for i in range(num):
        yield i

num = 1000
for i_num in gen_print(num+1):
    print(i_num)

