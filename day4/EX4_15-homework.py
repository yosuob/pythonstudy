'''
[회원가입]
아이디를 입력하세요(3글짜 이상)>>>
3글짜 이상 입력해주세요!

아이디를 입력하세요(3글짜 이상) >>>

패스워드를 입력하에쇼(영문 숫자 포함 8자 이상)>>>
>영문 숫자 포함 8자이상 입력해주세요

패스워드 곽인 한번더 입력하세요
>일치하지 않습니다. 다시 입력해주세요


패스워드를 입력하에쇼(영문 숫자 포함 8자 이상)>>>
>영문 숫자 포함 8자이상 입력해주세요

패스워드 곽인 한번더 입력하세요
>일치하지 않습니다. 다시 입력해주세요

회원 가입완료!!

[로그인]
아이디를 입력하세요 >>>
> 아이디가 일치하지 않습니다.

아이디를 입력하세요

패스워드를 입력하세요>>>
>패스워드가 일치하지 않습니다.

패스워드를 입력하세요>>>
로그인 성공
000님 환영합니다.:)
'''

id =[]
id_user =[]
pw_user = []
pw =[]
pw2 = []
print("[회원가입]")

while True:
    id = input("아이디를 입력하세요(3글자 이상) >>> ")
    if len(id) >2:
        break
    print("3글자 이상 입력해 주세요.")

while True:
    pw = input("패쓰워드를 입력하세요(영문 숫자 포함 8자이상) >>>")
    ch_count =0
    num_count =0

    for ch in pw:
        if ch.isalpha():
            ch_count += 1
        elif ch.isnumeric():
            num_count +=1

    if ch_count > 0 and num_count > 0 and ch_count + num_count >= 8:
        break
    else:
        print('영문 숫자 포함 8자이상 입력해 주세요!')

pw2 = input("패쓰워드 확인 한번 더 입력하세요 >>>")

if pw == pw2:
    print("회원가입 완료!!")
else:
    print("일치하지 않습니다! 다시 입력해 주세요!")

print("[로그인]")
while True:
    id_user = input("아이디를 입력하세요>>>")
    if id != id_user:
        print("아이디가 일치하지 않습니다.")
    else:
        break

while True:
    pw_user = input("패스워드를 입력하세요>>>")
    if pw != pw_user:
        print("패쓰워드가 일치하지 않습니다.")
    else:
        print("로그인 성공!!!")
        print("{}님 환영합니다.".format(id))
        break




