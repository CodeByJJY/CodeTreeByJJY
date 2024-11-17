from sortedcontainers import SortedSet
import sys

# 입력
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

# 초기화
s = SortedSet()
s.add(0)

min_length = sys.maxsize

for idx, val in enumerate(num):
    s.add(val)

    for point in s[:-1]:
        r_idx = s.bisect_right(point)

        if min_length > s[r_idx] - point:
            min_length = s[r_idx] - point
    
    print(min_length)