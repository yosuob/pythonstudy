'''

모듈(module)
    언제든지 변수 또는 클래스를 모아 놓은 파일을 모듈이라고 한다.

모듈 사용법
import 모듈명

'''

import converter

miles = converter.kilometer_to_milese(150)
print('150Km = {}miles'.format(miles))

pounds = converter.gram_to_pound(1000)
print('1000g = {}pound'.format(pounds))

