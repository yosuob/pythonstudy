'''

for 문과 dict

'''

eng_dict = {
    'sun' :'태양',
    'moon':'달',
    'star':'별',
    'space' : '우주'
}

eng_dict_keys = eng_dict.keys()

for word in eng_dict_keys:
    print('{} 의 뜻 : {}'.format(word,eng_dict.get(word)))

print(eng_dict)
for word in eng_dict:
    print('{} 의 뜻 : {}'.format(word,eng_dict.get(word)))
