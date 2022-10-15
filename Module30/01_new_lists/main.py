from typing import List
import math
floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

my_floats = map(lambda elem: round(elem**3, 3), floats)
my_names = [elem for elem in names if len(elem) >= 5]
my_numbers = math.prod(numbers)
