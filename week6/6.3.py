def calculate_area(radius):
    area = 3.14 * radius * 2
    return area

def get_sum(start, end):
    s = 0
    for i in range(start, end + 1):
        s += 1
    return s

x = get_sum(1, 10)
print('1부터 10까지의 합 : ', x)