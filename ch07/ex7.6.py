# (1)
name = ['한국', '미국', '중국', '필리핀']
distance = [100.2, 9834, 9597, 300]

city = list(zip(name, distance))
print('city = ', city)

# (2)
sudo = ['서울', '워싱턴', '베이징', '마닐라']
city_info = list(zip(name, sudo, distance))
print('city_info = ', city_info)