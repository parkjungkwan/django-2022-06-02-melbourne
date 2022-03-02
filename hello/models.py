from random import *

class Quiz01Calculator:
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def calc(self):
        self.add()
        self.sub()

    def add(self):
        return self.num1 + self.num2
    def sub(self):
        pass

class Quiz02Bmi(object):
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def getBmi(self):
        bmires =self.weight/(self.height*self.height)*10000
        if bmires > 25:
            return f'비만'
        elif bmires > 23:
            return f'과체중'
        elif bmires > 18.5:
            return f'정상'
        else:
            return f'저체중'

class Quiz03Grade(object):
    def __init__(self, name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def sum(self):
        return self.kor+self.eng+self.math
    def avg(self):
        return self.kor+self.eng+self.math /3

class Quiz04GradeAuto(object):
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math
    def avg(self):
        return self.kor + self.eng + self.math / 3
    def getGrade(self):
        pass
    def chkPass(self): # 60점이상이면 합격
        pass


class Quiz05Dice(object):
    def __init__(self):
        pass

class Quiz06RandomGenerator(object):
    def __init__(self): # 원하는 범위의 정수에서 랜덤값 1개 추출
        pass
class Quiz07RandomChoice(object):
    def __init__(self): # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜' , '권솔이', '김지혜' , '하진희' , '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]

class Quiz08Rps(object):
    def __init__(self):
        pass
class Quiz09GetPrime(object):
    def __init__(self):
        pass
class Quiz10LeapYear(object):
    def __init__(self):
        pass
class Quiz11NumberGolf(object):
    def __init__(self):
        pass
class Quiz12Lotto(object):
    def __init__(self):
        pass
class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass
class Quiz14Gugudan(object): # 책받침구구단
    def __init__(self):
        pass

if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1.계산기 (+, -,*,/) 2.bmi 3.Grade')
        if menu == '0':
            break
        elif menu == '1':
            q1 = Quiz01Calculator(int(input('첫번째 수')), int(input('두번째 수')))
            print(f'{q1.num1} + {q1.num2} = {q1.add()}')
        elif menu =='2':
            q2 = Quiz02Bmi(input('이름 : '), int(input('키 : ')), int(input('몸무게 : ')))
            print(f'이름: {q2.name}, 키: {q2.height}, '
                  f'몸무게: {q2.weight}, BMI상태: {q2.getBmi()} ')
        elif menu == '3':
            q3 = Quiz03Grade()
        elif menu =='4':
            q4 = Quiz04GradeAuto()
            for i in ['김유신', '강감찬', '유관순', '윤봉길', '신사임당']:
                print(i)
            kor = int(input('국어 : '))
            eng = int(input('영어 : '))
            math = int(input('수학 : '))
            #grade =Grade(name,kor,eng,math)
            #print(f'{name}님의 국어{kor} 영어{eng} 수학{math} 합계{grade.sum()} 평균{grade.avg()}')
        elif menu == '5':
            q5 = Quiz05Dice()
        elif menu == '6':
            q6 = Quiz06RandomGenerator()
        elif menu == '7':
            q7 = Quiz07RandomChoice()





