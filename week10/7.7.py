# 7.7 fruit_list 리스트에 대한 작업
fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon']

# (1) 가장 길이가 긴 문자열 출력하고, 리스트에서 삭제
max_length = len(max(fruit_list))  # 가장 긴 문자열의 길이 구하기

# 가장 긴 문자열을 가진 과일들을 원소로 갖는 리스트
longest_fruit = [fruit for fruit in fruit_list if len(fruit) == max_length]   

# 가장 길이가 긴 과일 출력
print(f'가장 길이가 긴 문자열 :, {longest_fruit[0]}, {longest_fruit[1]}')    

# 기존 리스트에서 가장 긴 문자열을 가진 과일들 제거
for fruit in longest_fruit:
    fruit_list.remove(fruit)

print('fruit_list =', fruit_list)  # 제거 후 리스트 출력
print('')

# (2) 문장 출력
print('banana : 문자열의 길이', len(longest_fruit[0])) # 6
print('orange : 문자열의 길이', len(longest_fruit[1])) # 6
print('kiwi : 문자열의 길이', len(fruit_list[0]))      # 4
print('apple : 문자열의 길이', len(fruit_list[1]))     # 5
print('melon : 문자열의 길이', len(fruit_list[2]))     # 5