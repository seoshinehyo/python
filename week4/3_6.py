# 3.6 2개의 정수 a, b를 입력 받아 a를 b로 나눈 몫과 나머지를 출력하는 프로그램

num1 = int(input("정수 a를 입력하시오 : ")) # 정수 a 입력 받기
num2 = int(input("정수 b를 입력하시오 : ")) # 정수 b 입력 받기

num_div = num1 // num2 # 정수 a를 b로 나눈 몫을 갖는 변수 num_div 선언
num_mod = num1 % num2 # 정수 a를 b로 나눈 나머지를 갖는 변수 num_mod 선언

print(f'a / b의 몫 : {num_div}') # 정수 a를 b로 나눈 몫 출력
print(f'a / b의 나머지 : {num_mod}') # 정수 a를 b로 나눈 나머지 출력
