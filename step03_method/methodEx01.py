'''
   def  함수명(인자):
       실행문장1
       실행문장1
       [return 리턴값]
'''

def view():          # 함수 정의
    print('hello')
    return

def view2():          # 함수 정의
    print('hello')

def view3():
    return 10

def view4():
    return 'Hi~~~~'

# 메인함수  : 프로그램의 엔트리 포인트
if __name__ == '__main__':
    view()  # 함수호출
    view2()
    # 리턴값 그냥 받기
    print(view3())
    # 리턴값 변수이용해서 받기
    str = view4();
    print(str)





