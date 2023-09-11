'''
 조건식이 참일 동안 실행문장 반복 수행
while 조건식:
   실행문장
   [탈출조건]
'''
'''
n = 10
while n>0:
    print(n)
    n = n-1
'''
# 단을 입력받아서 해당 단을 1~9까지 계산한 결과를 출력하시오.
dan = int(input('단을 입력하세요 ; '))
i = 1
while i < 10:
    print(dan , ' * ' , i , ' = ' , dan*i)
    i+=1
