s = 'Python is fun'

# print(s[10:13])

# print(s[:6])

# print(s[7:9])

print(s[0])
print(s[10:])
print(s[:6])
print(s[8:10])

city_info = [('서울', 9765), ('부산', 3441), ('인천', 2954), ('광주', 1501), ('대전', 1531)]
print(city_info[0])

for city in city_info:
    print(city[1])

print([x**2 for x in range(5) if x % 2 == 0])