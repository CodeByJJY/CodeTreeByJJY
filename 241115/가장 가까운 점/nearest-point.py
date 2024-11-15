#1. 원소 추가
#2. 최소 출력 & 최소 제거

# min-heap
import heapq

q = []

for _ in range(int(input())):
    x = int(input())
    if x > 0:
        heapq.heappush(q, x)
    else:
        if q:
            elem = heapq.heappop(q)
            print(elem)
        else:
            print(0)