#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def cal_day(m, d):
    month, day = 1, 1
    elapsed_day = 0

    while True:
        if month == m and day == d:
            break
        
        elapsed_day += 1
        day += 1

        if day > num_of_days[month]:
            month += 1
            day = 1
    
    return elapsed_day


m1, d1, m2, d2 = map(int, input().split())
A = input()

day_index = day_of_week.index(A)
result = (cal_day(m2, d2) - cal_day(m1, d1)) // 7
if (cal_day(m2, d2) - cal_day(m1, d1) + 1)%7 >= day_index:
    result += 1
print(result)