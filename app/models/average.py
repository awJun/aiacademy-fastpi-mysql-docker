class Average(object):
    def __init__(self, 국어_score, 영어_score, 수학_score, name):   # __init__ : 생성자
        self.국어_score = 국어_score             # 생성자에 속성 등록
        self.영어_score = 영어_score             # 생성자에 속성 등록
        self.수학_score = 수학_score             # 생성자에 속성 등록
        self.name = name
        self.avg = 0.0                           # 평균 계산을 하기 위해서 초기화
                                         
    def set_avg(self):        # get 읽기, set 쓰기
        self.avg = (self.국어_score + self.영어_score + self.수학_score)/3
        
        
    def get_avg(self):        # self가 있어야 전역변수
        return self.avg
        
    

    
    