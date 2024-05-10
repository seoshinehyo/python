dict1 = {'name' : '홍길동', 'age' : 20, 'address' : '서울시'}
print(dict1['name'])
del(dict1['address'])
print(dict1.get('name'))
print(dict1.keys(), dict1.values())
print(list(dict1.keys()), list(dict1.values()))
print(dict1.items())

for key in dict1.keys():
    print(dict1[key])

for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

student_list = [
    {'id' : 2021001, 'name' : '홍길동', 'kor' : 90, 'eng' : 80, 'math' : 70},
    {'id' : 2021002, 'name' : '김길동', 'kor' : 80, 'eng' : 70, 'math' : 60},
    {'id' : 2021003, 'name' : '이길동', 'kor' : 70, 'eng' : 60, 'math' : 50}
]

for student in student_list:
    print(student['id'], student['name'], student['kor'], student['eng'], student['math'])

# 과제 7.3, 7.7, 8.3