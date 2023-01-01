'''
모듈 사용법2
from 모듈명 import 함수
from 모듈명 import 함수1, 함수2
from 모듈명 import *
'''

from converter import kilometer_to_milese

miles = kilometer_to_milese(150)
print('150Km = {}miles'.format(miles))


