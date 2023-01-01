'''
method string
'''

# join
s = '-'.join("python")
print(s)

s = "+".join(['a', 'b', 'c', 'd', 'e'])
print(s)

s = "".join(['a', 'b', 'c', 'd', 'e'])
print(s)

#split() 메소드
s=' life is too short'
result = s.split()
print(result)

s='010-1234-5678'
result = s.split('-')
print(result)

data = "심요섭|20|프로그래머"
result = data.split("|")
print(result)
print("이름: {}".format(result[0]))

#replace()
s=' life is too short'
result = s.replace('short', 'long')
print(result)

#strip(), lstrip(), rstrop() 공백제거
s = '      apple'
print(s)
result = s.lstrip()#왼쪾공백 제거
print(result)

s = 'apple      '
result = s.rstrip()#오른쪽공백 제거
print(result)

s = '     apple      '
result = s.strip()#양쪾공백 제거
print(result)

#전체 공백 제거
s = 'a p p l e'
print(s)
result = s.replace(' ','')
print(s)
