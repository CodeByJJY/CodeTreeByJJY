import heapq

q = []  # 최소 힙 초기화

for _ in range(int(input())):
    x = int(input())
    if x > 0:
        heapq.heappush(q, x)  # 힙에 값 추가
    else:
        if q:
            print(heapq.heappop(q))  # 최소값 출력 및 제거
        else:
            print(0)  # 힙이 비어 있으면 0 출력
