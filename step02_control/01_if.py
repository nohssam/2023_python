import sys

print('수를 입력하세요 : ')
s1 = int(input())

# 파이썬 에서 타입 확인
# print(type(s1))

'''
if문
if s1 == 0 :
    print("0은 나눗셈을 이용할 수 없습니다.")
    sys.exit(0)

print('3/',s1 , '=' , 3/s1)
'''
# if ~ else
'''
if s1 == 0 :
    print("0은 나눗셈을 이용할 수 없습니다.")
else :
    print('3/',s1 , '=' , 3/s1)
'''

# 다중 if
if s1 >= 90 :
    print("A 학점")
elif s1 >= 80 :
    print("B 학점")
elif s1 >= 70 :
    print("C 학점")
else:
    print("F 학점")







