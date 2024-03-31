# 변수 선언과 출력
num1 = 10
num2 = 20
print(num1, num2)

# 하나의 변수에 두개의 값을 할당하면 튜플이 됨.
a = 100, 200
print(a)
print(a[1])
b = [100, 200]
print(b)

# 자료형 확인
print(type(123))
print(type('hello'))
print(type(12.2))
print(type([1, 2, 3, 4]))
print(type((1, 2, 3, 4)))
print(type({1, 2, 3}))
print(type({'a':10, 'b':20, 'c':30}))

# 산술 연산
print(num1 + num2)
print(num1 * num2 ** 2 / 100)

# 비교 연산
result = num1 == num2
print(result)

if (num1 > num2):
    print('num1이 num2보다 크다')
else:
    print('num1이 num2보다 작다')

# 논리 연산
login = False

if (num1 > 10 and num2 != 20):
    print('num1이 10보다 크고 num2가 20이 아닌 경우 실행')
if (num1 > 10 or num2 <= 20):
    print('num1이 10보다 크거나 num2가 20보다 작은 경우 실행')
if (not login):
    print('login 변수값이 false인 경우 실행')

# 할당 연산
num1 += 10
print(num1)

# 기타 연산
print(10 in [10, 20, 30])
num3 = num1
print(num1 is num3)
print(10 in {10, 20, 30})
print(10 in (10, 20, 30))