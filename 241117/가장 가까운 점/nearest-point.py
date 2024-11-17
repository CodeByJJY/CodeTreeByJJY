import heapq

# 입력
import sys
input = sys.stdin.read
data = input().split()

# n과 m
n, m = int(data[0]), int(data[1])

# 점 데이터
points = []
index = 2
for _ in range(n):
    x, y = int(data[index]), int(data[index + 1])
    index += 2
    # 힙에 삽입 (거리, x, y 순서)
    heapq.heappush(points, (abs(x) + abs(y), x, y))

# m번 반복
for _ in range(m):
    # 가장 가까운 점 꺼내기
    _, x, y = heapq.heappop(points)
    # 2씩 더한 값 다시 삽입
    heapq.heappush(points, (abs(x + 2) + abs(y + 2), x + 2, y + 2))

# 최종 원점에 가장 가까운 점 꺼내기
_, final_x, final_y = heapq.heappop(points)

# 출력
print(final_x, final_y)
