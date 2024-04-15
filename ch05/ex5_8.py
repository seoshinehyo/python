# 5.8 양의 정수를 입력받아 거꾸로 정수인지 판단하는 프로그램

while(True):
    num = input('정수를 입력하시오(-99 입력시 종료) : ')
    if (num == '-99'):                  # -99 입력시 프로그램 종료  
        print('프로그램을 종료합니다.')
        break

    if (len(num) < 3):                                  # 3자리 이상의 정수만 판단하도록 설정
        print('3자리 이상 입력하시오.')
    elif (len(num) == 3):                               # num이 3자리일때
        if (num[0] == num[2]):                          # 첫번째 문자와 마지막 문자가 같으면 거꾸로 정수
            print(f'{num}은(는) 거꾸로 정수입니다.')
        else:
            print(f'{num}은(는) 거꾸로 정수가 아닙니다.')
    elif (len(num) == 4):                               # num이 4자리일때
        if ((num[0] == num[3]) and (num[1] == num[2])): # 첫번째 문자와 네번째 문자가 같고, 두번째 문자와 세번째 문자가 같으면 거꾸로 정수
            print(f'{num}은(는) 거꾸로 정수입니다.')
        else:
            print(f'{num}은(는) 거꾸로 정수가 아닙니다.')
    elif (len(num) == 5):                               # num이 5자리일때
        if ((num[0] == num[4]) and (num[1] == num[3])): # 첫번째 문자와 다섯번째 문자가 같고, 두번째 문자와 세번째 문자가 같으면 거꾸로 정수
            print(f'{num}은(는) 거꾸로 정수입니다.')
        else:
            print(f'{num}은(는) 거꾸로 정수가 아닙니다.')



# while (True):
#     num = input("정수를 입력하시오 (-99를 입력하면 종료) : ")
#     if num == "-99":
#         break
#     if num == num[::-1]:
#         print(f"{num}은(는) 거꾸로 정수입니다.")
#     else:
#         print(f"{num}은(는) 거꾸로 정수가 아닙니다.")

    

