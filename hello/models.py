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


class Dice(object):
    def __init__(self):
        pass



if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1.계산기 (+, -,*,/) 2.bmi 3.Grade')
        if menu == '0':
            break
        elif menu == '1':
            calc = Quiz01Calculator(int(input('첫번째 수')), int(input('두번째 수')))
            print(f'{calc.num1} + {calc.num2} = {calc.add()}')
        elif menu =='2':
            bmi = Quiz02Bmi(input('이름 : '), int(input('키 : ')), int(input('몸무게 : ')))
            print(bmi.getBmi())
        elif menu == '3':
            pass
        elif menu =='4':
            for i in ['김유신', '강감찬', '유관순', '윤봉길', '신사임당']:
                print(i)
            kor = int(input('국어 : '))
            eng = int(input('영어 : '))
            math = int(input('수학 : '))
            #grade =Grade(name,kor,eng,math)
            #print(f'{name}님의 국어{kor} 영어{eng} 수학{math} 합계{grade.sum()} 평균{grade.avg()}')



