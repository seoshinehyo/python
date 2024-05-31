import csv

f = open("C:/Users/82105/Desktop/SSH/3-1/python/python/ch12/weather.csv", encoding='UTF-8')
data = csv.reader(f)
header = next(data)
for row in data:
    print(row[3], end=',')
f.close()