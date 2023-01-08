'''
예외처리 방법

try:
    코드작성 영역
except:
    예외 발생시 처리 영역


'''

try:
    a = int(input('제수를 입력하세요>>>'))
    b = int(input('피제수를 입력하세요>>>'))
    print('{} / [] = []'.format(a,b,a/b))
except:
     print('0으로 나누는 것은 불가능 합니다.')

