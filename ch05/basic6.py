# 리스트 선언 형태
list1 = [10, 20, 30, 40]
list2 = [i for i in range(1, 10)]
list3 = [0 for i in range(10)]
list4 = [0] * 10
print(list1)
print(list2)
print(list3)
print(list4)
print(sum(list1))

# 리스트 값 조작
list1.append(50)
list1[0] = 100
list1[1:2] = [200, 300]
list2[1] = [100, 200]
list2.insert(1,2)
del(list2[3])
list3.remove(0)

# 리스트 값 출력
print(list1)
print(list2)
print(list3)
print(list1[2:5])
print(list1[:3])

# 리스트 결합
print(list1 + list2)
print(list1 * 3)

# for문과 함께 사용시 유용한 방법들
for i, n in enumerate(list1):
    print(i, n)

for l1, l2 in zip(list1, list2):
    print(l1, l2)

# 기타
print(len(list1))
print(list1.pop())
print(list1)

print(list3.count(0))

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list1.reverse()
print(list1)

list5 = list1.copy()
list5.append(500)
print(list1)
print(list5)

