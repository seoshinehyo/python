# 10.2 넘파이를 활용한 문제
import numpy as np

# (1) 0~24 값을 갖는 5x5 크기의 2차원 행렬 n_arr 생성
n_arr = np.array([ [0, 1, 2, 3, 4],
                  [5, 6, 7, 8, 9],
                  [10, 11, 12, 13, 14],
                  [15, 16, 17, 18, 19],
                  [20, 21, 22, 23, 24]])
print(n_arr)
print()

# (2) n_arr의 첫 원소와 마지막 원소 인덱싱하여 출력
print(f'첫 원소 : {n_arr[0, 0]}')      # [0]이면 첫 번째 원소
print(f'마지막 원소 : {n_arr[-1, -1]}') # [-1] 사용해 마지막 원소 출력
print()

# (3) n_arr 슬라이싱 하여 배열 생성
n_arr3 = n_arr[0:2, :]
print(n_arr3)
print()

# (4) n_arr 슬라이싱 하여 배열 생성
n_arr4 = n_arr[2:, :]
print(n_arr4)
print()

# (5) n_arr 슬라이싱 하여 배열 생성
n_arr5 = n_arr[:, ::2]
print(n_arr5)
print()

# (6) n_arr 슬라이싱 하여 배열 생성
n_arr6 = n_arr[::2, ::2]
print(n_arr6)
print()

# (7) n_arr 슬라이싱 적용 후, reshape() 적용하여 배열 생성
n_arr7 = n_arr[:2, :]       # 슬라이싱 먼저 해주기
print(n_arr7.reshape(5, 2)) # reshape() 사용해 배열의 차원과 형태 변경