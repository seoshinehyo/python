stores = {'커피음료' : 7, '펜' : 3, '종이컵' : 2, '우유' : 8, '콜라' : 4, '책' : 5}



while (True):
    menu = input('메뉴를 선택하시오 1) 재고조회 2) 입고 3) 출고 4) 종료 : ')
    if (menu == '1'):
        name = input('[재고조회] 물건의 이름을 입력하시오: ')
        print('재고 : ', stores.get(name))
    elif (menu == '2'):
        pro1, num1 = input('[입고] 물건의 이름과 수량을 입력하시오 : ').split()
        stores[pro1] += int(num1)
        print(f'{pro1}의 재고 : {stores[pro1]}')
    elif (menu == '3'):
        pro2, num2 = input('[출고] 물건의 이름과 수량을 입력하시오 : ').split()
        stores[pro2] -= int(num2)
        print(f'{pro1}의 재고 : {stores[pro1]}')
    else:
        print('프로그램을 종료합니다.')
        break