# 3.10 두 점의 좌표를 입력 받아 두 점 사이의 거리를 출력하는 프로그램
import math

num_x1 = int(input('x1 좌표를 입력하시오 : ')) # x1 좌표 입력받기
num_y1 = int(input('y1 좌표를 입력하시오 : ')) # y1 좌표 입력받기
num_x2 = int(input('x2 좌표를 입력하시오 : ')) # x2 좌표 입력받기
num_y2 = int(input('y2 좌표를 입력하시오 : ')) # y2 좌표 입력받기

distance = math.sqrt(((num_x1 - num_x2) * (num_x1 - num_x2)) + ((num_y1 - num_y2) * (num_y1 - num_y2))) # 두 점 사이의 거리 distance

print(f'두 점의 거리 : {distance}')