from icecream import ic
import pandas as pd
class PandasQuiz(object):
    def __init__(self) -> None:
        pass
    
    '''
    Q1. 다음 결과 출력
        a  b  c
    1  1  3  5
    2  2  4  6
    ic| df1:       a  b  c   <-- 데이터 프레임에서는 키라고 부른다
                1  1  3  5
                2  2  4  6
    '''
    
    def quiz_01(self) -> None :
        df = pd.DataFrame.from_dict(
            {'1' : [ 1,  3,  5],'2' : [2,  4,  6]},
            orient='index',
            columns=['a', 'b', 'c'])
        ic(df)
                                                            # 인덱스 : 숫자키
                                                            # 스칼라 3개를 묶으면 다시 스칼라 묶엿으니
   
    #  Q3 두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
    def quiz_03(self) -> None :
        import random
        random_1 = [random.randint(10, 99) for p in range(0, 3)]
        random_2 = [random.randint(10, 99) for p in range(0, 3)]
        df = pd.DataFrame.from_dict(
            {'1' : random_1,'2' : random_2},
            orient='index',
            columns=['0', '1', '2'])
        ic(df)
    
    def quiz_04(self) -> None :
        import string
        import random
        
        _LENGTH = 5 # 5자리로 제한
        string_pool = string.ascii_letters
        result_1 = ""
        result_2 = ""
        result_3 = ""
        result_4 = ""
        result_5 = ""
        result_6 = ""
        result_7 = ""
        result_8 = ""
        result_9 = ""
        result_10 = ""

        for i in range(_LENGTH):
            result_1 += random.choice(string_pool)
            result_2 += random.choice(string_pool)
            result_3 += random.choice(string_pool)
            result_4 += random.choice(string_pool)
            result_5 += random.choice(string_pool)
            result_6 += random.choice(string_pool)
            result_7 += random.choice(string_pool)
            result_8 += random.choice(string_pool)
            result_9 += random.choice(string_pool)
            result_10 += random.choice(string_pool)
             
            random_1 = [random.randint(0, 99) for p in range(0, 4)]
            random_2 = [random.randint(0, 99) for p in range(0, 4)]
            random_3 = [random.randint(0, 99) for p in range(0, 4)]
            random_4 = [random.randint(0, 99) for p in range(0, 4)]
            random_5 = [random.randint(0, 99) for p in range(0, 4)]
            random_6 = [random.randint(0, 99) for p in range(0, 4)]
            random_7 = [random.randint(0, 99) for p in range(0, 4)]
            random_8 = [random.randint(0, 99) for p in range(0, 4)]
            random_9 = [random.randint(0, 99) for p in range(0, 4)]
            random_10 = [random.randint(0, 99) for p in range(0, 4)]
            
        df = pd.DataFrame.from_dict(
            {result_1 : random_1, result_2 : random_2, result_3 : random_3,
             result_4 : random_4, result_5 : random_5, result_6 : random_6,
             result_7 : random_7, result_8 : random_8, result_9 : random_9,
             result_10 : random_10
             },
            orient='index',
            columns=['국어', '영어', '수학', '사회'])
        ic(df)



#     # Q4 국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
#     # 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기
#     ''' 
#     ic| self.id(): 'HKKHc'
#     ic| self.score(): 22
#     ic| df4:        국어  영어  수학  사회
#             lDZid  57  90  55  24
#             Rnvtg  12  66  43  11
#             ljfJt  80  33  89  10
#             ZJaje  31  28  37  34
#             OnhcI  15  28  89  19
#             claDN  69  41  66  74
#             LYawb  65  16  13  20
#             QDBCw  44  32   8  29
#             PZOTP  94  78  79  96
#             GOJKU  62  17  75  49
#     https://hongku.tistory.com/297
#     '''
    









