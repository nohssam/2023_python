# https://pandas.pydata.org/
import pandas as pd
import pandasEx02 as ex02

# 한번에 value 값 계산 가능
div = ex02.city / 1000000
print(div)
print('-' * 30)

# 시리스 인덱싱
print(ex02.city[1])
print(ex02.city['대전'])
print('-' * 30)

# 배열 인덱싱을 사용할 경우 (순서, 변경 가능)
print(ex02.city[[1,3,0]])
print('-' * 30)

print(ex02.city[['대전','서울','부산']])
print('-' * 30)

# 슬라이싱
print(ex02.city[1:3])   # 3은 포함 되지 않는다.
print('-' * 30)

a = pd.Series(range(3) , index=['가', '1', 'A'])
print(a)
print('-' * 30)
print(a['A']) # 2
print(a.A)    # 2
print(a['1']) # 1
print(a.가)   # 0

# b = pd.Series(range(10,19))
# print(b)

