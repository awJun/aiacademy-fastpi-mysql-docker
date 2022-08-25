from app.models.user import User

class UserService(object):           # 명사로 이름지음
    def __init__(self) -> None:
        pass

    def calculate(self, id, password):                       # 동사로 이름지음
        calculator = User(id, password)         # 지역변수
        print(f"아이디 : {calculator.id}")   # {}안에는 기계어가 들어가는 자리
        print(f"비밀번호 : {calculator.password}")
        print("로그인에 성공되었습니다. ")

    
    