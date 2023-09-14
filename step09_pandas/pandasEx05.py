import pandas as pd

df = pd.read_csv("data/test_data.tsv", sep="\t")
# 열이 탭으로 구분 되어 있다면
# 만약 sep를 생략하면 기본적으로 콤마(,)로 구분한다.
print(df)
print(type(df))
print('-' * 30)
print(df.head(2))  # 상위 2개
print('-' * 30)
print(df.tail(2)) # 하위 2개

