fruit_dic = {'사과':0, '배':0, '수박':0, '귤':0, '포도':0}

p1, p2, p3, p4, p5 = input('사과, 배, 수박, 귤, 포도 가격을 공백으로 구분하여 입력: ').split()
price = [p1, p2, p3, p4, p5]

for i, fruit in enumerate(fruit_dic):
    fruit_dic[fruit] = price[i]

print(fruit_dic)

print('-------------- 오늘의 과일 가격 ----------------')
for fruit in fruit_dic.keys():
    print(f'{fruit}        :        {fruit_dic[fruit]} 원')

name = input('구매를 원하는 과일의 이름을 입력하시오 : ')
print(f'오늘의 수박 가격은 {fruit_dic[name]} 원 입니다.')