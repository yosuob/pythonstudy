'''
JSON (JavaScript Object Notation)
    - 딕셔너리 비슷하다
    - 구조
    { K : V }

잡스 형님 -> 아이폰 -> 대 멀티디바이스 시대!
-> 모든 기기 통신 가능 시대 -> 프로토콜(통신큐칙) -> http 시대
-> javascript 시대 -> json 시대
->  xml 시대는 끝났다

'''

import json

# 방법1
'''
dict_list =[
    {
        'name': 'james',
        'age' : 20,
        'spec':[
            175.5,
            70.5
        ]
    },
    {
        'name': 'alice',
        'age' : 21,
        'spec':[
            168.5,
            46.5
        ]
    }
]

json_string = json.dumps(dict_list)

with open("dictList.json", 'w') as file:
    file.write(json_string)
print('')
'''

# 방법 2
dict_list =[
    {
        'name': 'james',
        'age' : 20,
        'spec':[
            175.5,
            70.5
        ]
    },
    {
        'name': '홍길동',
        'age' : 21,
        'spec':[
            168.5,
            46.5
        ]
    }
]

json_string = json.dumps(dict_list,indent=4, ensure_ascii=False)
# indent 들여쓰기 , ensure_acsii False 한글 읽기
with open('dictList.json','w',encoding= "UTF-8") as file:
    file.write(json_string)

print("dictlist.json 파일이 생성되었습니다.")


