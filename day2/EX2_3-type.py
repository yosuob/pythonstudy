'''
내장 데이터 유형
    python 변수는다른 유형의 데이터를 저장할 수 있으며
    다른 유형은 다른 작업을 수행할 수 있다.


텍스트 유형 : str
숫자 유형 : int, float, complex
시퀀스 유형 : list, tuple, rage
매핑 유형 : dict
세트 유형 : set
부울(논리) 유형 : bool
바이너리 유형 : bytes, bytearray
없음 유형 : NoneType
'''

#str
x = "hello world"
print(type(x))

#int
x=20
print(type(x))

#float
x= 20.5
print(type(x))
#complex
x=1j
print(type(x))
#list
x=["a", "b", "c"]
print(type(x))
#tuple
x=("a", "b", "c")
print(type(x))
#range
x = range(6)
print(type(x))
#dict
x={"name" : "amy","age" : "20"}
print(type(x))
#set
x={"a", "b", "c"}
print(type(x))
#bool
x=True
print(type(x))