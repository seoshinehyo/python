# 도전문제 2.6 - 2
# num1 = float(input('첫 번째 실수를 입력하세요: '))
# num2 = float(input('두 번째 실수를 입력하세요: '))
# sum = num1 + num2
# avg = sum / 2.0
# print('두 수의 합은 ', sum, ' 두 수의 평균은 ', avg)

# 함수 선언만 해두고 내용은 추후 구현하고자 할때
def printAll():
    pass

# 인자가 하나인 함수
def printName(name):
    prtMsg = name + ' Hello'
    print(prtMsg)
printName('홍길동')

# 인자가 두개이고 리턴이 있는 함수
def calc(num1, num2):
    return num1 + num2

print('계산결과: ', calc(200, 300))
print('계산결과: ', calc(num1 = 200, num2 = 300))

# 가변 인자 // 배열도 가능
def total(*num):
    tot = 0
    for n in num:
        tot += n
    return tot

t = total(1, 2)
print(t)
t = total(1, 5, 2, 6)
print(t)
print(total(1, 2, 3))

# 리턴이 여러개인 함수, 가변인자 사용

def addNum(*nums):
    tot = 0
    cnt = 0
    for n in nums:
        tot += n
        cnt += 1
    return cnt, tot

cnt, tot = addNum(10, 20, 30)
print(cnt, tot)

# 매개변수 유형에 따른 caller 값 변경 여부
# 원시 자료형은 immutable로 값이 복사되어 전달
# list, dictionary 같은 객체는 mutable로 레퍼런스만 전달되어 caller 값도 변경
num3 = 10     # immutable
m = [1, 2, 3] # mutable

def varChange(num3, m):
    num3 = num3 + 1 ## 함수 안에서 immutable한 값 변경 불가능
    m.append(0) ## 리스트에 0 추가

varChange(num3, m)
print(num3, m) # 10 [1, 2, 3, 0] 출력. num3는 immutable이기 때문

# 전역 변수, 지역 변수, global, nonlocal

num4 = 10
def varTest():
    # global num4
    num5 = 100
    global num4
    num4 = 100

varTest()
print(num4)
#print(num5) 오류



