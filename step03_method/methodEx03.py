# 연속한 숫자 누적의 합을 구하는 알고리즘
# 입력 : n
# 출력 : 1 부터 n 까지 연속한 숫자의 누적합

def sum_sq(n):
    s=0  # 저장 변수
    for i in range(1, n+1):
        s = s + i
    return s

print(sum_sq(10))
print(sum_sq(100))