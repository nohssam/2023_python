# https://pandas.pydata.org/
import pandas as pd

# 시리즈 생성
# 2017년 도시별 인구 데이터
city = pd.Series([9857426, 1502227, 2475231, 3470653],
                 index=['서울', '대전', '대구', '부산'])

if __name__ == '__main__':
    print(city)
    print(type(city))
