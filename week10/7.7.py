# 7.7 fruit_list 리스트에 대한 작업
fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon']

# (1) 가장 길이가 긴 문자열 출력하고, 리스트에서 삭제
max_length = len(max(fruit_list))
longest_fruit = [fruit for fruit in fruit_list if len(fruit) == max_length]

print('가장 길이가 긴 문자열 :', longest_fruit)

for fruit in longest_fruit:
    fruit_list.remove(fruit)

print('fruit_list =', fruit_list)
print('')

# (2) 문장 출력
print('banana : 문자열의 길이', len(longest_fruit[0]))
print('orange : 문자열의 길이', len(longest_fruit[1]))
print('kiwi : 문자열의 길이', len(fruit_list[0]))
print('apple : 문자열의 길이', len(fruit_list[1]))
print('melon : 문자열의 길이', len(fruit_list[2]))