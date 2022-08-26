# uvicorn main:app --reload
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calcuator import CalculatorService
from app.services.user import UserService
from app.services.average import AverageService

def print_menu():
    print("0. 전체프로그램 종료")
    print("1. 계산기 프로그램")
    print("2. 로그인 프로그램")
    print("3. 성적표 프로그램")
    menu = input("메뉴 선택")
    return menu
 
def main():    # 메소드
    # print_menu()    # 메소드 식
    while 1:   # 구문    /  while 1: 무한반복
        menu = print_menu()
        if menu == "0":
            print("전체 프로그램을 종료합니다.")
            break
        
        elif menu == '1':
            calculatorService = CalculatorService()    #  / CalculatorService() : 생성자  식? 
            first = int(input('\n첫번째 값 입력2: \n'))
            secund = int(input('두번째 값 입력: \n'))
            calculatorService.calculate(first, secund)     # .이있으면 메소드(.이 없으면 함수)
        
        elif menu == '2':
            userService = UserService()    #  / CalculatorService() : 생성자  식? 
            id = str(input('\n아이디를 입력하세요 : \n'))
            password = str(input('비밀번호를 입력하세요 : \n'))
            userService.user(id, password)     # .이있으면 메소드(.이 없으면 함수)
        
        elif menu == '3':
            averageService = AverageService()    #  / CalculatorService() : 생성자  식? 
            name = input('\n학생의 이름을 입력하세요 : \n')
            국어_score = int(input('국어 점수를 입력하세요 : \n'))
            영어_score = int(input('영어 점수를 입력하세요 : \n'))
            수학_score = int(input('수학 점수를 입력하세요 : \n'))
            평균 = averageService.get_평균(name, 국어_score, 영어_score, 수학_score)     # .이있으면 메소드(.이 없으면 함수)
            print(f"이름 : {name} 학점: {평균}")

if __name__ == '__main__':
    main()


# main은 마지막 부분 즉, 최종 출력 부분이므로 객체가 들어오면 안된다 그래서 여기서는 함수로 받아야한다.
# 객체로 안받으려면 self를 사용안하면 함수로 받아준다.


# 식은 변수를 리턴하는 곳  /  변수는 값을 받는곳  /  식2개 문2개 변수2
# 문: 조건문 / 반복문
# 변수 : 지역변수, 전역변수
# for while차이는 리미트가 있냐 없냐 차이 while은 리미트 걸어줘야함


# 지금 수업 때 하는 것은 아키텍쳐이다.




