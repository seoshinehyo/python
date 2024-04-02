# 3.12 각 입체도형의 부피의 근사값을 구하는 프로그램 구현

import math

pi = 3.14 # 원주율 값

# 1. 모서리의 길이가 13인 정육면체의 부피
cube_edge1 = 13 # 정육면체 모서리 길이
cube_volume1 = cube_edge1 * cube_edge1 * cube_edge1 # 정육면체 부피 계산
print(f'모서리의 길이가 13인 정육면체의 부피의 근사값 : {cube_volume1}') # 정육면체 부피 출력

# 2. 모서리의 길이가 22인 정육면체의 부피
cube_edge2 = 22 # 정육면체 모서리 길이
cube_volume2 = cube_edge2 * cube_edge2 * cube_edge2 # 정육면체 부피 계산
print(f'모서리의 길이가 22인 정육면체의 부피의 근사값 : {cube_volume2}') # 정육면체 부피 출력

# 3. 가로, 세로, 깊이가 각각 17, 25, 16인 직육면체의 부피
cuboid_width = 17 # 직육면체 가로
cuboid_height = 25 # 직육면체 세로
cuboid_depth = 16 # 직육면체 깊이
cuboid_volume = cuboid_width * cuboid_height * cuboid_depth # 직육면체 부피 계산
print(f'가로, 세로, 깊이가 각각 17, 25, 16인 직육면체의 부피의 근사값 : {cuboid_volume}') # 정육면체 부피 출력

# 4. 반지름과 높이가 각각 10, 15인 원뿔 부피
cone_radius = 10 # 원뿔 반지름
cone_height = 15 # 원뿔 높이
cone_volume = 1 / 3 * pi * cone_radius * cone_radius * cone_height # 원뿔 부피 계산
print(f'반지름과 높이가 각각 10, 15인 원뿔의 부피의 근사값 : {cone_volume}') # 정육면체 부피 출력

# 5. 반지름이 25인 구 부피
sphere_radius = 25 # 구 반지름
sphere_volume = 4 / 3 * pi * sphere_radius * sphere_radius * sphere_radius # 구 부피 계산
print(f'반지름이 25인 구 부피의 근사값 : {sphere_volume}') # 구 부피 출력

# 6. 반지름과 높이가 각각 10, 15인 원기둥
cylinder_radius = 10 # 원기둥 반지름
cylinder_height = 15 # 원기둥 높이
cylinder_volume = pi * cylinder_radius * cylinder_radius * cylinder_height # 원기둥 부피 계산
print(f'반지름과 높이가 각각 10, 15인 원기둥의 근사값 : {cylinder_volume}') # 원기둥 부피 출력

# 7. math.pi 값을 이용해 (4), (5), (6) 다시 풀기
cone_radius = 10 # 원뿔 반지름
cone_height = 15 # 원뿔 높이
cone_volume = 1 / 3 * math.pi * cone_radius * cone_radius * cone_height # 원뿔 부피 계산
print(f'math.pi 값을 이용한 반지름과 높이가 각각 10, 15인 원뿔의 부피의 근사값 : {cone_volume}') # 정육면체 부피 출력

sphere_radius = 25 # 구 반지름
sphere_volume = 4 / 3 * math.pi * sphere_radius * sphere_radius * sphere_radius # 구 부피 계산
print(f'math.pi 값을 이용한 반지름이 25인 구 부피의 근사값 : {sphere_volume}') # 구 부피 출력

cylinder_radius = 10 # 원기둥 반지름
cylinder_height = 15 # 원기둥 높이
cylinder_volume = math.pi * cylinder_radius * cylinder_radius * cylinder_height # 원기둥 부피 계산
print(f'math.pi 값을 이용한 반지름과 높이가 각각 10, 15인 원기둥의 근사값 : {cylinder_volume}') # 원기둥 부피 출력