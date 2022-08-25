from app.models.calculator import Calculator

class CalculatorService(object):           # 명사로 이름지음
    def __init__(self) -> None:
        pass

    def calculate(self, first, second):                       # 동사로 이름지음
        calculator = Calculator(first, second)         # 지역변수
        print(f"첫번째수: {calculator.first}")   # {}안에는 기계어가 들어가는 자리
        print(f"두번째수: {calculator.second}")
        print(f"{calculator.first} + {calculator.second} = {calculator.sum()}")
        print(f"{calculator.first} - {calculator.second} = {calculator.subtract()}")
        print(f"{calculator.first} * {calculator.second} = {calculator.multiply()}")
        print(f"{calculator.first} / {calculator.second} = {calculator.division()}")
        
    
    
    
    
    