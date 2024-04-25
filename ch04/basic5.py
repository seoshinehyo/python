# # input() 함수를 이용한 입력

# num = input('숫자를 입력하세요: ')
# print(num)

# # 입력값을 숫자로 변환
# num = eval(input('숫자를 입력하세요: '))
# print(num)
# num = int(input('숫자를 입력하세요: '))
# print(num)
# num = int(input('숫자를 입력하세요(16진수): '), 16)
# print(num)

num = 42
print(str(num) + '은 ' + str(num) + '입니다.')

print(num, '은 ', num, '이다.')

second = int(input('초를 입력하세요 : '))

hour = second // 3600
minute = (second - hour * 3600) // 60
s = (second - hour * 3600) % 60

print(str(hour) + '시간 ' + str(minute) + '분 ' + str(s) + '초')