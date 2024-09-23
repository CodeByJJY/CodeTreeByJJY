#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 2024년은 윤년이므로 2월이 29일
#                 0.     1.     2.     3.     4.     5.     6.
day_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def cal_day(m, d):
    month, day = 1, 1
    elapsed_day = 0

    while True:
        if month == m and day == d:
            break
        
        elapsed_day += 1
        day += 1

        if day > num_of_days[month]:  # 해당 월의 일수를 넘어가면 다음 달로 이동
            month += 1
            day = 1
    
    return elapsed_day


m1, d1, m2, d2 = map(int, input().split())
A = input()

# m1, d1이 월요일이므로 첫 번째 요일이 'Mon'인 상태
start_day_index = cal_day(m1, d1) % 7  # m1, d1 날짜에 해당하는 요일을 계산
target_day_index = day_of_week.index(A)  # 찾으려는 요일의 인덱스

# m1, d1부터 m2, d2까지의 날짜 차이를 계산
date_interval = cal_day(m2, d2) - cal_day(m1, d1) + 1

# m1, d1부터 m2, d2까지 A 요일이 몇 번 등장하는지 계산
# date_interval // 7는 A 요일이 포함된 주의 수, date_interval % 7는 남은 일수에서 A 요일이 있는지 확인
day_count = (date_interval // 7) + (1 if (start_day_index + (date_interval % 7)) % 7 >= target_day_index else 0)

print(day_count)