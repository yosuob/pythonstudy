'''
지역 변수(local)
    함수 내부선언
    함수 내부에서만 사용가능

전역변수(gloabl)
    함수 외부 선언
    함수 내부외부 모두 사용가능


'''

gVar ='전역'
def globalAndlocal():
    lVar ="지역"
    print(gVar,'변수 입니다.')# 전역 변수 참조만 하고 있다.
    print(lVar, '변수 입니다.')

globalAndlocal()



gVar ="전역"
def globalAndlocal():
    lVar ="지역"
    gVar = '변경된 전역이 아닌 새로운 지역'
    print(gVar,'변수 입니다.')
    print(lVar, '변수 입니다.')

globalAndlocal()

print(gVar)

#전역 변수 선언
total =0
def gift(dic,who,money):
    global total # 전역 변수 total를 사용하겠다.
    total += money
    dic[who] = money

wedding = {}
gift(wedding, '영희',5)
gift(wedding,"철수",6)

print('축의금 명단: {}'.format(wedding))
print('전체 축이금: {}'.format(total))




