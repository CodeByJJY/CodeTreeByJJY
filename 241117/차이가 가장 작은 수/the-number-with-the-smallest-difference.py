from sortedcontainers import SortedSet
import sys

# 입력
n, m = map(int, sys.stdin.readline().split())
s1 = SortedSet()
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    s1.add(num)

# 차이값 계산
min_diff = float('inf')
l, r = 0, 1  # 투 포인터 초기화

while r < len(s1):
    diff = s1[r] - s1[l]
    if diff >= m:
        min_diff = min(min_diff, diff)
        l += 1  # 왼쪽 포인터 이동
    else:
        r += 1  # 오른쪽 포인터 이동

if min_diff == float('inf'):
    print(-1)
else:
    print(min_diff)
