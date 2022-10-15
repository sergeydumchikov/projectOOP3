from collections import Counter

def polindrom(val: str) -> bool:
    return len(list(filter(lambda x: x % 2, Counter(val).values()))) <= 2


print(polindrom('abcba'))
print(polindrom('abbbc'))
