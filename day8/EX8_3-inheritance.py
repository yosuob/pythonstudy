'''

죽음의 다이아몬드

'''

class A:
    def greeting(self):
        print('안녕하세요 A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요.B입니다.')


class C(A):
    def greeting(self):
        print('안녕하세요.C입니다.')


class D(C,B):
   pass # 내부동작 필요없고 빈껍데기만 필요할떄 pass 사용


X = D()

X.greeting()
print(D.mro())
