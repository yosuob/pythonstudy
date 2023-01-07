'''

파일 복사

파일 복사
    원본  ->  버퍼 변수(memory)   -> 복사존
'''

buffer_size = 1024 # 1024byte로 1KB 의미
with open("hello.txt", 'rb') as source:
    with open('hello2.txt', 'wb') as copy:
        while True:
            buffer = source.read(buffer_size) # 1024BYTE 단위로 읽겠다.
            if not buffer:
                break
            copy.write(buffer)
print('hello2.txt 파일이 복사되었습니다.')

