# bts = ['V', 'J-Hope', 'RM', 'Jungkook', 'Jin', 'Jimin', 'Suga']
# for i in bts:
#     print(i)

n = int(input('정수를 입력하시오: '))
fact = 1
for i in range(n+1, 1, -1):
    fact = fact * i

print(n, '!은', fact, "이다.")