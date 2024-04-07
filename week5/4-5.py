# 4.5 random.randint(0, 9)를 사용하여 0~9 사이의 복권번호 3개를 만들고, 사용자로부터 3개의 정수를 입력 받아 상금을 알려주는 프로그램
import random

user1, user2, user3 = input("세 개의 값을 입력하세요: ").split() # 사용자로부터 세 개의 복권번호를 입력받기

# 입력 받은 값이 문자이기 때문에 int형으로 casting(랜덤 복권 번호가 randint로 int형이기 때문)
user1 = int(user1) 
user2 = int(user2)
user3 = int(user3)

# 랜덤 복권 번호 3개 입력 받기
rand1 = random.randint(0, 9)
rand2 = random.randint(0, 9)
rand3 = random.randint(0, 9)


num = 0; # 맞은 개수 초기값 0
if ((user1 == rand1) or (user1 == rand2) or (user1 == rand3)):
    num += 1 # 값 맞으면 맞은 개수 +1
if ((user2 == rand1) or (user2 == rand2) or (user2 == rand3)):
    num += 1 # 값 맞으면 맞은 개수 +1
if ((user3 == rand1) or (user3 == rand2) or (user3 == rand3)):
    num += 1 # 값 맞으면 맞은 개수 +1
 
if num == 3:
    print('상금 1억원') # 3개 다 맞으면 1억원
elif num == 2:
    print('상금 1천만원') # 2개 맞으면 1천만원
elif num == 1:
    print('상금 1만원') # 1개 맞으면 1만원
else:
    print('다음 기회에...') # 0개 맞으면 다음 기회에 출력
