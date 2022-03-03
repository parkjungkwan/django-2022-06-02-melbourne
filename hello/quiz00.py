if __name__ == '__main__':
    while 1:
        menu = input('"00계산기 01Bmi 02주사위 03가위바위보 04윤년 05숫자추론 06로또 07예약 08입출금 09구구단"')
        if menu == '0':
            break
        elif menu == '1':
            q1 = Quiz01Calculator(int(input('첫번째 수')), int(input('두번째 수')))
            print(f'{q1.num1} + {q1.num2} = {q1.add()}')
        elif menu == '2':
            member = Member()
            q2 = Quiz02Bmi()
            member.name = input('이름 : ')
            member.height = float(input('키 : '))
            member.weight = float(input('몸무게 : '))
            res = q2.getBmi(member)
            print(f'이름: {member.name}, 키: {member.height}, '
                  f'몸무게: {member.weight}, BMI상태: {res} ')
        elif menu == '3':
            q3 = Quiz03Grade()
        elif menu == '4':
            q4 = Quiz04GradeAuto()
            for i in ['김유신', '강감찬', '유관순', '윤봉길', '신사임당']:
                print(i)
            kor = int(input('국어 : '))
            eng = int(input('영어 : '))
            math = int(input('수학 : '))
            # grade =Grade(name,kor,eng,math)
            # print(f'{name}님의 국어{kor} 영어{eng} 수학{math} 합계{grade.sum()} 평균{grade.avg()}')
        elif menu == '5':
            print(Quiz05Dice.cast())
        elif menu == '6':
            q6 = None
        elif menu == '7':
            q7 = Quiz07RandomChoice()
            print(q7.chooseMember())
        elif menu == '8':
            q8 = Quiz08Rps(1) # 가위 1 바위 2 보 3
            print(q8.game())