# 8.3 학번, 이름, 전화번호의 3쌍의 요소를 갖는 student_tup 튜플
student_tup = (('241101', '박동윤', '010-1234-4500'), ('241102', '김은지', '010-2230-6540'), 
               ('241103', '이지은', '010-3232-7788'))

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
print('')

# (3) student_tup 마지막 항목에 직전학기의 학점 추가
student_list = list(student_tup)   # 튜플은 변경 불가능하므로 리스트로 변경

# 각 요소에 학점 추가
student_list[0] = student_list[0] + (4.3,)
student_list[1] = student_list[1] + (3.9,)
student_list[2] = student_list[2] + (4.25,)

# 리스트를 딕셔너리로 변환
for student in student_list:
    student_dict[student[0]] = [student[1], student[2], student[3]]

# 학생 정보 출력
print("학생의 정보 목록")
for key, value in student_dict.items():
    print(f"{{'{key}' : {value}}}")
print('')

# (4) 3 학생의 평균값 출력
sum = 0
# for문을 통해 학점 합 구하기
for key in student_dict.keys() :
    sum = sum + student_dict[key][2]
 
# 소수점 둘째 자리까지 캐스팅하여 학점 평균 출력 
print("전체 학생의 학점 평균 : ", "{:.2f}".format(sum / len(student_dict.keys()))) 
