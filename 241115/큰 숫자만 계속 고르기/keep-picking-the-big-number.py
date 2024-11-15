import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))

q = []

for elem in A:
    heapq.heappush(q, -elem)

for _ in range(M):
    #1. 최대값 뽑기
    elem = -heapq.heappop(q)

    #2. elem-1 넣기
    heapq.heappush(q, -(elem-1))

print(-q[0])