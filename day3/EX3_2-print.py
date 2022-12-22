'''
print() 함수  사용법

'''


print("재미있는","파이썬")
print("python", "java", "C",sep =",")

print("안녕",end="")
print("하세요")


fos = open("sample.txt" , mode = "wt")
print('print("hello WOrld")',file = fos)
fos.close()

