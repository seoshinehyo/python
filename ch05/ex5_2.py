# (1) for 반복문과 while 반복문을 사용해 1~100까지의 정수 중 홀수의 합 출력

# for문 사용
sum1 = 0
for i in range(100):
    if (i % 2 == 1):
        sum1 += i
    
print(f'1에서 100까지의 수 중에서 홀수의 합(for) : {sum1}')

# while문 사용
sum2 = 0
i = 0
while (i < 100):
    if (i % 2 == 1):
        sum2 += i
    i += 1

print(f'1에서 100까지의 수 중에서 홀수의 합(while) : {sum2}')

# (2) for 반복문과 while 반복문을 사용해 1~100까지의 정수 중 짝수의 합 출력

# for문 사용
sum3 = 0
for i in range(100):
    if (i % 2 == 0):
        sum3 += i
    
print(f'1에서 100까지의 수 중에서 짝수의 합(for) : {sum3}')

# while문 사용
sum4 = 0
i = 0
while (i < 100):
    if (i % 2 == 0):
        sum4 += i
    i += 1

print(f'1에서 100까지의 수 중에서 짝수의 합(while) : {sum4}')

# (3) 사용자로부터 시작 정수와 끝 정수 입력으로 받아 사이 정수들의 합을 구하는 프로그램
num1 = int(input('시작 정수를 입력하세요 : '))
num2 = int(input('끝 정수를 입력하세요 : '))

sum5 = 0
i = num1
while (i <= num2):
    sum5 += i
    i += 1

print(f'{num1} 에서 {num2} 까지 정수의 합 : {sum5}')