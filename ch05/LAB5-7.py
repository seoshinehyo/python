# dan = int(input('단 입력: '))
i = 1
j = 1

while (i <= 9):
    j = 1
    while (j <= 9):
        print('%s * %s = %s' % (i, j, i * j))
        j += 1
    i += 1