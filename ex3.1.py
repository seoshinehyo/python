# time = (int)(input('초를 입력하세요: ')) # 10000초
# time_h = time // 3600
# time_m = (time - time_h * 3600) // 60
# time_s = (time - time_h * 3600) % 60 # - time_m * 60도 가능

# print(f'입력한 시간은 {time_h} 시간 {time_m} 분 {time_s} 초입니다.')


# num = 7 #0111
# val = 7
# v1 = 7 // 2
# va = 7 % 2

# v2 = v1 // 2
# vb = v1 % 2

# v3 = v2 // 2
# vc = v2 % 2

# print


# BMI 계산 
xy = int(input('여성이면 1, 남성이면 0을 입력하세요: '))
height = int(input('당신의 키는 얼마입니까? '))
hurry = int(input('당신의 허리 둘레는 얼마입니까? '))

RFM = 64 - (20 * (height / hurry)) + 12 * xy
print(f'당신의 RFM은 {RFM}')