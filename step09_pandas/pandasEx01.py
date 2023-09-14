# https://pandas.pydata.org/
import pandas as pd

# v1 = pd.Series([92600,94200,92100,94300,98700])
# print(v1)

# v1 = pd.Series([1000,3000,5000,2000], index=['18-11', '19-11', '20-11', '21-11'])
# print(v1)

s1 = pd.Series([20,140,30],index=['kt', 'sk', 'lg'])
s2 = pd.Series([10,30,20],index=['naver', 'kakao', 'goole'])
print(s1)
print("*"*50)
print(s2)
print("*"*50)
s3 = pd.Series([150,40,330],index=['kt', 'lg', 'sk'])
hap = s1 + s3  # index들이 같지만 순서가 다른 두개의 Series를 만들어 합친 경우
print(hap)

print("******** 인덱스만 출력 **********")
for i in hap.index:
    print(i, end='  ')
print()

print("******** 값만 출력 **********")
for i in hap.values:
    print(i, end=' ')
print()
