import heapq, sys

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

# 최대 힙으로 변환하기 위해 부호 반전
pq = []
for elem in nums:
    heapq.heappush(pq, -elem)

# m번 연산 수행
for _ in range(m):
    # 최대값 꺼내고 감소시킨 뒤 다시 삽입
    max_val = -heapq.heappop(pq)  # 부호 반전으로 최댓값 가져오기
    heapq.heappush(pq, -(max_val - 1))

# 최댓값 출력
print(-pq[0])  # 부호 반전으로 원래 값 출력
