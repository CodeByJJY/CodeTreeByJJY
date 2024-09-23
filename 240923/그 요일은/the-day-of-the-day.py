#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#                 0.     1.     2.     3.     4.     5.     6.
day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1, d1, m2, d2 = map(int, input().split())
A = input()

date_itv = (sum(num_of_days[0:m2]) + d2) - (sum(num_of_days[0:m1]) + d1)

date_cnt = date_itv // 7

if date_itv%7 >= day_of_week.index(A):
    date_cnt += 1

print(date_cnt)