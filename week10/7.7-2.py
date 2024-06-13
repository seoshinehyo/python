fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon']

max_length = len(max(fruit_list))

fruit_list2 = [fruit for fruit in fruit_list if len(fruit) < max_length]

print(f'fruit_list = {fruit_list2}')

for fruit in fruit_list:
    print(f'{fruit} : 문자열의 길이 {len(fruit)}')