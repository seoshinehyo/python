# 8.3 학번, 이름, 전화번호의 3쌍의 요소를 갖는 student_tup 튜플
student_tup = (('241101', '박동윤', '010-1234-4500'), ('241102', '김은지', '010-2230-6540'), 
               ('241103', '이지은', '010-3232-7788'))


student_dic = {}

for i in range(len(student_tup)):
    student_dic[student_tup[i][0]] = list(student_tup[i][1:])

print('학생의 정보 목록')
print(student_dic)

num = input('학번을 입력하시오 : ')
mem = student_dic[num]

print(f'이름 : {mem[0]}')
print(f'연락처 : {mem[1]}')

student_list = [list(student) for student in student_tup]

score = [4.3, 3.9, 4.25]

for i in range(len(student_list)):
    student_list[i].append(score[i])


student_dic2 = {}

for i in range(len(student_list)):
    student_dic2[student_list[i][0]] = student_list[i][1:]

print(student_dic2)

for key in student_dic2.keys() :
    sum = sum + student_dic2[key][2]

avg = sum / 3

print(f'전체 학생의 학점 평균 : {avg}')