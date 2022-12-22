'''
dictionary
    KEY:VALUE 로 이루어져 쌍응로 데이터 값을 지정하는데 사용


'''


#dict 선언
thisdict ={
    "brand" :'구찌',
    "model" : "g2003",
    "year" : 2022
}
print(thisdict)

'''
키 이름을 사용하여 참조할 수 있다
'''

# 값 가져오기
thisdict ={
    "brand" :'구찌',
    "model" : "g2003",
    "year" : 2022
}
print(thisdict["brand"])
print(thisdict.get("model"))

# 키 목록 가져오기
print(thisdict.keys())

#추가하기
thisdict ={
    "brand" :'구찌',
    "model" : "g2003",
    "year" : 2022
}
thisdict["color"] ="red"
print(thisdict)
thisdict.update({"bgclor" : "blakc"})

#변경하기
thisdict["color"]="yellow"
thisdict.update({"bgcolor" : "blue"})
print(thisdict)

# 제거하기
thisdict.pop("model")
print(thisdict)

#마지막 삽입된 항목 제거하기
thisdict.popitem()
print(thisdict)










