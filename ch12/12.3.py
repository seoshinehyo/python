import csv

f = open("C:/Users/82105/Desktop/SSH/3-1/python/python/ch12/weather.csv", encoding='UTF-8')
data = csv.reader(f)
header = next(data)
max_wind = 0.0

for row in data:
    if row[2] == '' :
        wind = 0
    else :
        wind = float(row[2])
    
    if max_wind < wind :
        max_wind = wind

print('지난 10년간 울릉도의 최대 풍속은 ', max_wind, 'm/s')
f.close()