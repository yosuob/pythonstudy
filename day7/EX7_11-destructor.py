'''

소멸자
    인스턴스가 소멸될 떄 자동으로 호출 된다.
'''

class Sercice:
    def __init__(self,service=None):
        self.service = service
        print('{} service가 시작되었습니다.'.format(self.service))

    def __del__(self):
        print('{} service 가 종료되었습니다.'.format(self.service))

s = Sercice('길 안내')

del s

s2 = Sercice()

print('프로그램 종료!')