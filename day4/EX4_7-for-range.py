'''
for뮨과 range 함수


range()
    연속된 숫자를 만들어주는 함수
'''
dan = int(input("출력할 구구단을 입력하세요>>>"))
for n in range(1,10, 2):
    print('{} x {} = {} \t'.format(dan , n, dan*n))
'''
range(stop)
'''

# 0 ~ 9 range
for n in range(10):
    print('{} x {} = {} \t'.format(dan , n, dan*n))

'''
rnage (start,stop)
'''
# 1~9 range
for n in range(1,10):
    print('{} x {} = {} \t'.format(dan , n, dan*n))

'''
range(start, stop, step)
'''
# 1부터 2씩 증가 < 10
for n in range(1, 10, 2):
    print('{} x {} = {}'.format(dan, n, dan * n), end='')
print()
