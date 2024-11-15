from sortedcontainers import SortedSet
import sys

n = int(sys.stdin.readline())  # 입력 크기
nums = list(map(int, sys.stdin.readline().split()))  # 입력 배열

s = SortedSet()
s.add(0)  # 초기값으로 0 추가

minimum = []

for i in nums:
    s.add(i)  # 값 삽입 (O(log n))
    
    # 가까운 값 계산
    idx = s.bisect_left(i)  # 현재 값의 위치 (왼쪽 경계)
    
    closest_diff = float('inf')  # 초기 최소값
    if idx > 0:
        closest_diff = min(closest_diff, i - s[idx - 1])  # 이전 값과 차이
    if idx < len(s) - 1:
        closest_diff = min(closest_diff, s[idx + 1] - i)  # 다음 값과 차이
    
    minimum.append(closest_diff)  # 최소 차이 저장

    print(min(minimum))
