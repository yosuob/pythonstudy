'''
for문
    값의 범위나 횟수가 정해져 있을떄
    사용하면 편리한 반복문
    while문 보다 자주 사용된다.

for 변수 in 반복가능한 객체:
    반복실행문
'''

pwd = input("비밀번호를 입력하세요>>")
ch_count =0
num_count =0

for ch in pwd:
    if ch.isalpha():
        ch_count += 1
    elif ch.isnumeric():
        num_count +=1

if ch_count > 0 and num_count > 0:
    print("가능한 비밀번호 입니다.")
else:
    print('불가능한 비밀번호 입니다.')

# pwd = input('비밀번호를 입력하세요 >>> ')
pwd = 'abcdefg55'
     # 012345678

ch_count = 0
num_count = 0
for ch in pwd:
    if ch.isalpha():
        ch_count += 1
    elif ch.isnumeric():
        num_count += 1

if ch_count > 0 and num_count > 0:
    print('가능한 비밀번호 입니다.')
else:
    print('불가능한 비밀번호 입니다.')