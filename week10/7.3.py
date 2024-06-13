# 7.3 두 개의 리스트를 사용해 모든 조합을 생성하여 출력

# 리스트 2개 생성
list1 = ['I like', 'I love']
list2 = ['pancakes.', 'kiwi juice.', 'espresso.']

print(list1[0], list2[0]) # I like pancakes.
print(list1[0], list2[1]) # I like kiwi juice.
print(list1[0], list2[2]) # I like espresso.
print(list1[1], list2[0]) # I love pancakes.
print(list1[1], list2[1]) # I love kiwi juice.
print(list1[1], list2[2]) # I love espresso.

print(list1[0] + ' ' +  list2[0])