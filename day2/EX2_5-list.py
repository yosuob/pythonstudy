'''
list
    단일 변수에 여러 항목을 저장하는데 사용된다
    list 항목은 순서가 지정되고 변경 가능하며 중복값 허용
    list 에는 다양한 데이터 유형이 포함될 수 있다.

'''

thislist=["a", "b", "c"]

print(thislist)
print(thislist[0])
#list길이
print(len(thislist))

list1=["a", "b", "c"]
list1=[1, 2, 3]
list1=[Ture, False, False]

#다양한 유형 포함 가능
lsit4 =["abc", 34 , False , 40]

#항목 접근
list1=["a", "b", "c"]
print(thislist[1])

#변경
list1=["a", "b", "c"]
list1[1] ="avd"
print(list1)

list1=["a", "b", "c", "d","e","f"]
list1[1:3] =["x","y"]
print(list1)

#두번쨰 세번째 값을 하나의 값으로 변경
list1=["a", "b", "c", "d","e","f"]
list1[1:3] =["x"]
print(list1)

#항목추가
list1=["a", "b", "c", "d","e","f"]
list1.append("wow")
print(list1)

#항목추가 - 인덱스 번호로 추가
list1=["a", "b", "c", "d","e","f"]
list1.insert(1,"test")
print(list1)

#항목 값으로 제거
list1=["a", "b", "c", "d","e","f"]
list1.remove("a")
print(list1)


#항목을 지정된 인덱스로 제거
list1=["a", "b", "c", "d","e","f"]
list1.pop(2)
print(list1)

#마지막값제거
list1=["a", "b", "c", "d","e","f"]
list1.pop()
print(list1)

#목록삭제
list1=["a", "b", "c", "d","e","f"]
list1.clear()
print(list1)

#확장
list1=["a", "b", "c", "d","e","f"]
list1.extend(["f","g"])
print(list1)

#객체 삭제
del list1
print(list1)



