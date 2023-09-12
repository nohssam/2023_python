class Calc:
    #초기화 메서드 : 생성자 , 객체가 생성될때 무조건 자동으로 실행(호출)
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self, first, second):
      result  = first + second
      return result;

    def sub(self, first, second):
        result  = first - second
        return result;

    def div(self, first, second):
        result  = first / second
        return result;
# 상속(Calc 클래스는 부모클래스가 된다.)
class MoreCalc(Calc):
   def __init__(self):
       print("자식 객체 생성")

    # 오버라이딩 : 부모메서드를 가져와서 자기에 맞게 변경하는 것 (자식이 우선 순위가 높다)
   def div(self, first, second):
       if second == 0:
           return "0으로 나눌 수 없습니다."
       else:
            result  = first / second
            return result;

# 자식은 부모의 것을 마음대로 사용할 수 있다.
a = MoreCalc()
b = a.add(7,3)
print(b)
c = a.sub(7,3)
print(c)
d = a.div(7,3)
print(d)
e = a.div(7,0)
print(e)
