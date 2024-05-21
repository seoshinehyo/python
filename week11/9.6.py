# 9.6 문장 분석해 점수의 합과 평균점수 출력하는 프로그램
s = 'English = 89, Science = 90, Math = 92, History = 80.'
s2 = s.replace(',', '').replace('.', '') # 문장 s에서 ,와 .을 공백으로 변경

words = s2.split() # 문자열 s2를 split해서 리스트로 만들기
scores = [] # 점수를 담을 빈 리스트 선언

# 반복문을 사용해 문자열이 숫자면 int형으로 캐스팅해 score 리스트에 집어넣기
for num in words:
    if num.isdigit():
        scores.append(int(num))

print(f'문장 s : {s}') # 문장 출력
print(f'총점 : {sum(scores)}') # 총점 출력
print(f'평균점수 : {sum(scores) / len(scores)}') # 평균점수 출력
