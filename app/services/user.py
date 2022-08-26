from app.models.user import User

class UserService(object):           # 명사로 이름지음
    def __init__(self) -> None:
        pass

    def user(self, id, password):                       # 동사로 이름지음
        calculator = User(id, password)         # 지역변수
        if calculator.id != "youngjun" and  calculator.password != '1234':
            print(f"\n아이디 비밀번호가 일치하지않습니다 다시 입력해주세요. \n")
        else:
            print(f"\n아이디 \n: {calculator.id}" + f"\n비밀번호 \n: {calculator.password}")   # {}안에는 기계어가 들어가는 자리
            print("(아이디가 비밀번호가 일치합니다.)\n") 
                   

    
    