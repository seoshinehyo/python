def add(num1, num2):
    return num1 + num2
print(add(10, 20))

def longin(id, pwd):
    if (id == "hong" and pwd == "1234"):
        return True
    else:
        return False
   
num = 2   
if (num % 2 == 1):
    print("홀수")
else:
    print("짝수")
print("홀수" if num % 2 == 1 else "짝수")

names = ['김', '이', '박']
for name in names:
    print(name)

for i in range(1,10,2):
    print(i)

# for cnt in range(3):
#     uname = input('# 아이디를 입력하세요: ')
#     passwd = input('# 비번을 입력하세요: ')
#     if((uname == "hong") and (passwd == "1234")):
#         print('>> 로그인 성공!!')
#         break
#     else:
#         print('>> 아이디 혹은 비번이 틀렸습니다!!')
# else:
#     print('>> 3회이상 틀려서 종료합니다!!')
#     exit()

# for i in range(3):
#     uname = input('# 아이디를 입력하세요: ')
#     passwd = input('# 비밀번호를 입력하세요: ')
#     if (uname == 'hong' and passwd == '1234'):
#         print('>> 로그인 성공')
#         break
#     else:
#         print('>> 오류')
# else:
#     print('>> 3회 이상 틀려서 종료합니다')
    
names = ['kim', 'lee', 'park']
count = 0
while (count < len(names)):
    print(names[count])
    count += 1

