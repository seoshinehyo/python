import random

# 가위1 바위2 보3

user = int(input('가위-1, 바위-2, 보-3 : '))
com = random.randrange(1, 4)

if (user == com):
    print('비겼습니다.')
else:
    if ((user == 1) and (com == 2)):
        print('졌습니다.')
    if ((user == 1) and (com == 3)):
        print('이겼습니다')
    if ((user == 2) and (com == 3)):
        print('졌습니다.')
    if ((user == 2) and (com == 1)):
        print('이겼습니다')
    if ((user == 3) and (com == 1)):
        print('졌습니다.')
    if ((user == 3) and (com == 2)):
        print('이겼습니다')

