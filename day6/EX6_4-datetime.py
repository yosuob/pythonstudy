'''

datetime
    날짜와 시간 데이터를 처리할 때 사용한다.
'''

import datetime

#현재 날짜와 시간 변환, 마이크로초 단위 출력
print(datetime.datetime.now())
print(datetime.datetime.today())

#date() 함수 특정 날짜를 만들어 변환
print(datetime.date(2022,12,4))

print(datetime.time(10,40,0))

y = datetime.datetime.now().year
m = datetime.datetime.now().month
d = datetime.datetime.now().day

print('{}년 {}월 {}일'.format(y,m,d))

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
print(yesterday)
tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)

date1 = datetime.date(2022,11,4)

date2 = datetime.date(2022,12,4)
print(date2 -date1)
print(
    (date2 -date1).total_seconds()
    )

