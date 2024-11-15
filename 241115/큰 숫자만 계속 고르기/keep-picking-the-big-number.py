import heapq
import sys

# 입력 처리
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

# 최대 힙 생성
max_heap = []
for num in nums:
    heapq.heappush(max_heap, -num)  # 부호 반전하여 최대 힙처럼 사용

# m번 작업 수행
for _ in range(m):
    largest = -heapq.heappop(max_heap)  # 최댓값 가져오기 (부호 복원)
    heapq.heappush(max_heap, -(largest - 1))  # 감소 후 다시 삽입

# 최댓값 출력
print(-max_heap[0])  # 힙의 최댓값 (부호 복원)
