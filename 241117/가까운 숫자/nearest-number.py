from sortedcontainers import SortedSet
import sys

# 입력
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

# 초기화
s = SortedSet()
s.add(0)
min_len = sys.maxsize

# 점 추가 및 거리 계산
for idx, val in enumerate(num):
    if idx == 0:
        # 새 점 추가
        s.add(val)
        min_len = s[1] - s[0]
        print(min_len)
    else:
        # 새 점 추가
        s.add(val)

        # 이웃 점 계산
        idx = s.index(val)  # 새 점의 위치
        left_dist = float('inf') if idx == 0 else val - s[idx - 1]
        right_dist = float('inf') if idx == len(s) - 1 else s[idx + 1] - val

        # 최소 거리 출력
        min_len = min(left_dist, right_dist, min_len)
        print(min_len)
