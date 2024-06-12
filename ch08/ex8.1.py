phone_book = {'홍길동': '010-1234-5678',
              '강감찬': '010-1234-5678',
              '이순신': '010-1234-5678'}

phone_book.pop('홍길동')

for name in phone_book.keys():
    print(name, ':', phone_book[name])

for name, number in phone_book.items():
    print(name, ':', number)

contact = {'성': '홍',
           '이름': '길동',
           '직장': '삼성'}

for key in contact.keys():
    print(key, ':', contact[key])

sort = sorted(phone_book)
print(sort)

print(sorted(phone_book.items()))