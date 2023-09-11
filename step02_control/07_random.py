# 난수 함수
# from random import random
from random import *

# 0.0 이상 1.0미만의 임의의 실수
print(random())
# 1.0 이상 3.0미만
print(uniform(1.0, 3.0))
# 1 이상 10이하(포함)
print(randint(1, 10))

# 1-10미만
print(randrange(1,10))

# [] 안에 존재하는 값중 하나 선택
print(choice([1,54,9,32,75,11]))