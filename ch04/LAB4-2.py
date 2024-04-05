#(1)
age = int(input('나이를 입력하시오: '))

if (age >= 15):
    print('본 영화를 보실 수 있습니다.')
    print('영화의 가격은 10000원입니다.')
else:
    print('영화를 보실 수 없습니다.')
    print('다른 영화를 보시겠어요?')

#(2)
card = input('카드의 종류를 입력하세요(청소년, 성인): ')
if (card == '청소년'):
    print('청소년입니다.')
else:
    print('승인되었습니다.')