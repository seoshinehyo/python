num1 = 100
num2 = 200

print(num1, num2)
print(num1, num2, sep=',')
print('Hello', 'World', sep='-')
#print('num1=' num1, ',', 'num2=', num2)
print('num1=%d, num2=%d' % (num1, num2))
print(f'num1={num1}, num2={num2}')
print('A', 'B', 'C', sep='/')
print('A', 'B', 'C', end='\n\n')

name = '홍길동'
age = 20
print('이름: {0}, 나이: {1}'.format(name, age))
print('이름 3회 반복: {0}, 나이 2회 반복: {1}'.format(name*3, age*2))
print(f'이름: {name}, 나이: {age}')