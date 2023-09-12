# 예외처리
# try:
#     오류가 발생할 수 있는 구문
# except Exception as e:
#     오류발생
# else :
#     오류가 발생하지 않음
# finally:
#     무조건 마지막에 실행

try:
  4/0
except Exception as e:
    print(e)
    print("오류발생")
# else :  생략가능
   #print("오류발생하지 않음")
finally:
    print("수고 하셨습니다.")