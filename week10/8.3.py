# 8.3 학번, 이름, 전화번호의 3쌍의 요소를 갖는 student_tup 튜플
student_tup = (('241101', '박동윤', '010-1234-4500'), ('241102', '김은지', '010-2230-6540'), ('241103', '이지은', '010-3232-7788'))

# (1) 튜플 수정해 { 학번 : [이름, 전화번호] } 쌍의 딕셔너리로 바꾸기
student_dict = {} # 빈 딕셔너리 생성

# 튜플을 반복하여 딕셔너리에 추가
for item in student_tup:
    student_dict[item[0]] = [item[1], item[2]]

# 딕셔너리 출력
print('학생의 정보 목록')
for key, value in student_dict.items():
    print(f"{{'{key}' : ['{value[0]}', '{value[1]}']}}")
print('')

# (2) 학생의 학번을 입력으로 받아 이름과 전화번호 출력하는 학사 정보 프로그램
student_id = input('학번을 입력하시오 : ')
print(f'이름 : {student_dict[student_id][0]}')
print(f'연락처 : {student_dict[student_id][1]}')
