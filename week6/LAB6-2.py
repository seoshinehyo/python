def weekly(rate, hour):
    if (hour >= 30):
        return rate * 30 + 1.5 * (hour - 30) * rate
    else:
        return rate * hour

rate = int(input('시급을 입력하시오 : '))
hour = int(input('근무 시간을 입력하시오 : '))

print(f'주급은 {weekly(rate, hour)}')
print('주급은 ' + str(weekly(rate, hour)))
print('주급은 {0}'.format(weekly(rate, hour)))
print('주급은', weekly(rate, hour))
