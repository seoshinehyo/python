# 9.7 카이사르 암호 문장과 함께 이동시킬 칸 수를 입력받아 암호문 생성하는 프로그램
import string
src_str = string.ascii_uppercase + string.ascii_lowercase

s = input('문장을 입력하시오 : ')
n = int(input('이동시킬 칸 수를 입력하시오 : '))

dst_str = ''

# 반복문을 통해 암호화된 문자열 dst_str 완성하기
for char in s:
    if char in src_str: # 문자일때
        index = src_str.index(char) # 문자의 index 구하기
        encrypted_index = (index + n) % len(src_str) # n칸 이동한 문자의 index 구하기
        encrypted_char = src_str[encrypted_index] # encrypted_index로 n칸 이동된 문자 찾기
        dst_str += encrypted_char # n칸 이동한 문자 dst_str 문자열에 넣기
    else: # 문자를 제외한 숫자나 쉼표와 같은 특수문자일때
        dst_str += char

print("암호화된 문장 : ", dst_str)