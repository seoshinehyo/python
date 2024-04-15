# 5.2-(1) for 반복문과 while 반복문을 사용해 1~100까지의 정수 중 홀수의 합 출력

# for문 사용
sum1 = 0
for i in range(1, 101): # 1~100 100번 반복
    if (i % 2 == 1): # 홀수
        sum1 += i    # sum1 변수에 홀수값 더하기
    
print(f'1에서 100까지의 수 중에서 홀수의 합(for) : {sum1}')

# while문 사용
sum2 = 0
i = 1
while (i <= 100):     # 1~100 100번 반복
    if (i % 2 == 1): # 홀수
        sum2 += i    # sum2 변수에 홀수값 더하기
    i += 1           # i 값 1씩 더해주기

print(f'1에서 100까지의 수 중에서 홀수의 합(while) : {sum2}')

# 5.2-(2) for 반복문과 while 반복문을 사용해 1~100까지의 정수 중 짝수의 합 출력

# for문 사용
sum3 = 0
for i in range(1, 101): # 1~100 100번 반복
    if (i % 2 == 0): # 짝수
        sum3 += i    # sum3 변수에 짝수값 더하기
    
print(f'1에서 100까지의 수 중에서 짝수의 합(for) : {sum3}')

# while문 사용
sum4 = 0           
i = 1
while (i <= 100):     # 1~100 100번 반복
    if (i % 2 == 0): # 짝수
        sum4 += i    # sum4에 짝수값 더하기
    i += 1           # 1씩 더해주기

print(f'1에서 100까지의 수 중에서 짝수의 합(while) : {sum4}')

# 5.2-(3) 사용자로부터 시작 정수와 끝 정수 입력으로 받아 사이 정수들의 합을 구하는 프로그램
num1 = int(input('시작 정수를 입력하세요 : '))  # num1 입력 받기
num2 = int(input('끝 정수를 입력하세요 : '))    # num2 입력 받기

sum5 = 0
i = num1            # 시작 정수 num1을 i로 설정
while (i <= num2):  # 끝 정수 num2까지 반복
    sum5 += i       # 정수 하나씩 더하기
    i += 1          # i 1씩 num2까지 더하기

print(f'{num1} 에서 {num2} 까지 정수의 합 : {sum5}')