# dict
dict1 = {2021001:'홍길동', 2021002:'김사랑', 2021003:'나대장'}
del(dict1[2021003])
print(dict1)
print(dict1.keys(), dict1.values())
print(list(dict1.keys()), list(dict1.values()))
print(dict1.items())

# key로 전체값 출력
for key in dict1.keys():
    print(dict1[key])

# 전체 값만 출력
for value in dict1.values():
    print(value)

# 키가 있는지 확인, 주로 if와 사용
if (2021001 in dict1):
    print(True)
