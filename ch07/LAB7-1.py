# fruits = list() # fruits = []

# for i in range(3):
#     name = input('좋아하는 과일 이름을 입력하시오: ')
#     fruits.append(name)

# fruit = input('과일의 이름을 입력하세요: ')
# answer = fruit in fruits

# if (answer == True):
#     print('이 과일은 당신이 좋아하는 과일입니다.')
# else:
#     print('이 과일은 당신이 좋아하는 과일이 아닙니다.')




# # 하도 세화 동쪽, 빛의 벙커, 더 클리프, 쇠소깍, 서연의 집
# # 오설록, 마라도, 동명정류장 카페, 스누피가든, 루나폴, 
# # 비밀의숲, 자구리해변, 꽃돈, 명성목장, 







fruits = []
for i in range(3):
    fruit_name = input('좋아하는 과일 이름을 입력하시오: ')
    fruits.append(fruit_name)

name = input('과일의 이름을 입력하세요: ')

if (name in fruits):
    print('이 과일은 당신이 좋아하는 과일입니다.')
else:
    print('이 과일은 당신이 좋아하는 과일이 아닙니다.')






