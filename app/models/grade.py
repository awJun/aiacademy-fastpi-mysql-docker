class Grade(object):
    def __init__(self,name, kor,eng,math) :
        self.name = name 
        self.kor = kor
        self.eng = eng
        self.math = math
        self.avg = 0.0    # 평균 계산을 하기 위해서 초기화
        
    def set_avg(self):    # get 읽기, set 쓰기
        self.avg = (self.kor + self.eng + self.math)/3
    
    def get_avg(self):    # self가 있어야 전역변수
        return self.avg
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    