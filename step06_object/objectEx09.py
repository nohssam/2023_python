class Calc:
    #초기화 메서드 : 생성자 , 객체가 생성될때 무조건 자동으로 실행(호출)
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
      result  = self.first + self.second
      return result;

# 상속(Calc 클래스는 부모클래스가 된다.)
class MoreCalc(Calc):
    # 아무것도 하지 않으려면
    pass

# 자식은 부모의 것을 마음대로 사용할 수 있다.
a = MoreCalc(4,9)
print(a.add())

