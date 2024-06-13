s = 'English = 89, Science = 90, Math = 92, History = 80.'
s2 = s.replace('=', '').replace(',', '').replace('.', '')

words = s2.split()

sum = 0
scores = words[1::2]

for i in range(4):
    sum += int(scores[i])


print(f'총점 : {sum}')
print(f'평균점수  {sum / len(scores)}')