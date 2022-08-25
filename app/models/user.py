class User(object):
    def __init__(self, id, password):     # 메소드    / None은 return임
        self.id = id
        self.password = password
    
    def calculate(self):
        if self.id != "youngjun":
            print("아이디가 틀렸습니다. ")
        elif self.password != "1234":
            print("비밀번호가 틀렸습니다. ")        
        else:
            return self.id =="youngjun" and self.password =="1234"


    
    
    
    
    
    
    
    
    
    
    