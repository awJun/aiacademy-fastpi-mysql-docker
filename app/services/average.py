from app.models.average import Average

class AverageService(object):           # 명사로 이름지음
    def __init__(self) -> None:
        self.credit = 0

    def set_score(self, name, 국어_score, 영어_score, 수학_score):                       # 동사로 이름지음
        average = Average(name, 국어_score, 영어_score, 수학_score)         # 지역변수
        average.set_avg()
        avg = average.get_avg()
        
        if avg >= 90:
            self.credit = "A"
        elif avg >= 80:
            self.credit = "B"
        elif avg >= 70:
            self.credit = "C"
        elif avg >= 60:
            self.credit = "D"
        elif avg >= 50:
            self.credit = 'E'
        else:
            self.credit = "F"
        
    def get_평균(self, name, 국어_score, 영어_score, 수학_score):
        self.set_score(name, 국어_score, 영어_score, 수학_score)
        return self.credit










