'''
튜플
    단일 변수에 여러 항목을 저장하는데 사용된다
    순서가 있고, 변경할 수 없는 list
    둥근 괄호로 작성된다
'''

thistuple =("a",'B',"c")
print(thistuple)

#튜플값 변경 방법
thistuple =("a",'B',"c")
thiscast =list(thistuple)
thiscast[1] ="잠만보"
thistuple = tuple(thiscast)
print(thistuple)

#ㅍ튜플 압축풀기
thistuple =("a",'B',"c")
(p1,p2,p3,p4)=thistuple
print(p1)
print(p2)
print(p3)
print(p4)

#두개 튜플 조인
thistuple1= ("피카츄","라이츄","파이리","꼬부기")
thistuple2= ("버터플","야도란","피죤투","또가스")
thistuple3 = thistuple1 + thistuple2
print(thistuple3)
