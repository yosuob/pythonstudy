'''
divmod
    두 숫자를 인자로 전달 받아
    첫번째 인자르 ㄹ두번쨰 인자로
    나눈 몫과 나머지를 tuple 형식으로 반환한다

'''

money = 10000
price = 3000
result = divmod(money, price)
print("빵을 {}개 사고 {}원이 남았스빈다.".format(result[0],result[1]))