class Calculator(object):
    def __init__(self, first, second):   # __init__ : 생성자
        self.first = first               # 생성자에 속성 등록
        self.second = second             # 생성자에 속성 등록
                                         # self.first과 self.second는 ()가 없으므로 속성이다.
    # 위에서 만든 속성으로 활용       
    def sum(self):                         # sum은()가 있으므로 메소드
        return self.first + self.second
    
    def subtract(self):
        return self.first - self.second

    def multiply(self):
        return self.first * self.second
    
    def division(self):
        return self.first / self.second