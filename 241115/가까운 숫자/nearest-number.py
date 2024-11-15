from sortedcontainers import SortedSet
import sys

n = int(sys.stdin.readline())  # 입력 크기

nums = list(map(int, sys.stdin.readline().split()))  # 입력 배열
s = SortedSet()
s.add(0)  # 초기값으로 0 추가

minimum = []

for i in nums:
    s.add(i)  # 각 값을 SortedSet에 추가

    for j in range(len(s) - 1):
        x = s[j]
        idx = s.bisect_right(x)  # x 다음 위치 찾기
        if idx < len(s):  # 범위를 벗어나지 않도록 확인
            minimum.append(s[idx] - x)  # 최소 차이 계산

    print(min(minimum))
