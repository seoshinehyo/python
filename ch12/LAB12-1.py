import csv
import matplotlib.pyplot as plt

f = open("C:/Users/82105/Desktop/SSH/3-1/python/python/ch12/weather.csv", encoding='UTF-8')
data = csv.reader(f)
header = next(data)

monthly_wind = [0 for x in range(12)]
days_counted = [0 for x in range(12)]

for row in data:
    month = int(row[0][5:7])
    if (row[3] != ''):
        wind = float(row[3])
        monthly_wind[month-1] += wind
        days_counted[month-1] += 1

for i in range(12):
    monthly_wind[i] /= days_counted[i]

plt.plot(monthly_wind, 'blue')
plt.show()

f.close()