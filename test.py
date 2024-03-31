print("hello python")
stepA = 15
stepB = 13
stepC = 8

for i in range(60 * 17+1):
    if 20 < i <= 60 * 16:
        if i % stepA == 0 and i % stepC == 0:
            print(f'BUS A | BUS C 동시 운행\t : \t{(60 * 6 + i) // 60}시 {(60 * 6 + i) % 60}분 ')
        if i % stepC == 0 and i % stepB == 0:
            print(f'BUS B | BUS C 동시 운행\t : \t{(60 * 6 + i) // 60}시 {(60 * 6 + i) % 60}분 ')
# 주석 추가
    if i % stepA == 0 and i % stepB == 0:
        print(f'BUS A | BUS B 동시 운행\t : \t{(60 * 6 + i) // 60}시 {(60 * 6 + i) % 60}분 ')