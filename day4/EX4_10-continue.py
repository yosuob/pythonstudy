'''
continue
    while 문이나 for 문과 같은
    반복문을 강제로 건너뛰기

'''

total =0
for a in range(1,101):
    if a % 3 ==0: # 3의 배수
        continue
    print('a:{}, total {}'.format(a,total))
    total += a
print(total)