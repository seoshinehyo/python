stores = {'커피음료' : 7, '펜' : 3, '종이컵' : 2, '우유' : 8, '콜라' : 4, '책' : 5}

name = input('물건의 이름을 입력하시오: ')
print('재고 : ', stores.get(name))