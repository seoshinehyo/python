# dan = int(input('단 입력: '))
i = 1
j = 1

while (i <= 9):
    j = 1
    while (j <= 9):
        print('%s * %s = %s' % (i, j, i * j))
        j += 1
    i += 1

# 시험은 8주차 금요일 9시10분부터 시험, 중첩 반복문 구구단 시험문제 ㄷㄷ

# 이번주 과제는 5.2, 5.3, 5.8
# 5.8이 문제가 어려워 거꾸로해도 같은 정수 121 3443 원래의 값과 같은 정수.


for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')

# print('%s * %s = %s' % (i, j, i * j))