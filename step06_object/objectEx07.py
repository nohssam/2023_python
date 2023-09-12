class Book:
    #초기화 메서드 : 생성자 , 객체가 생성될때 무조건 자동으로 실행(호출)
    def __init__(self):
        print("책 객체를 새로 만들었어요")

    def setData(self,title,price, author):
        self.title = title
        self.price = price
        self.author = author

    def printData(self):
        print('제목 : ' , self.title)
        print('가격 : ' , self.price)
        print('저자 : ' , self.author)

