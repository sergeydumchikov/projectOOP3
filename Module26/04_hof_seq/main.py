def QHofstaditer(start: list):
    """
    Функция описывающая Последовательность Хофштадтера

    """
    if start == [1, 2]: return
    seq = start[:]
    while 1:
        q = seq[-seq[-1]] + seq[-seq[-2]]
        seq.append(q)
        yield q
        if q > 1000:
            return


starter = [1, 1]
for elem in QHofstaditer(starter):
    print(elem)
