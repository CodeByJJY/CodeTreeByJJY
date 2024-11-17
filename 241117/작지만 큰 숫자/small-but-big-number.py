import sys
from sortedcontainers import SortedSet

# 입력
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
s_num = SortedSet(num)  # 중복 제거와 정렬
q = list(map(int, sys.stdin.readline().split()))

# 질의 처리
for query in q:
    # 질의 숫자보다 작거나 같은 수 중 최댓값 탐색
    idx = s_num.bisect_right(query) - 1  # bisect_right로 query 초과 위치 찾고 -1
    if idx >= 0:  # 유효한 숫자가 존재할 경우
        print(s_num[idx])
        s_num.discard(s_num[idx])  # 숫자 제거
    else:  # 유효한 숫자가 없는 경우
        print(-1)
