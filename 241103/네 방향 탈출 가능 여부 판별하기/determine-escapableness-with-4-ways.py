# 알고리즘 변경
# dx, dy 테크닉에서 변화를 주어야 함
from collections import deque

q = deque()

# n행 m열
n, m = tuple(map(int, input().split()))

# visited 배열
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

# 격자
grid = []
for _ in range(n):
    grid.append(tuple(map(int, input().split())))

# dx, dy
#      상,하,좌,우
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

# push 함수
def push(x, y):
    visited[x][y] = True
    q.append((x, y))

# 격자 내 여부 탐색
def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

# 이동 가능 여부 탐색
def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

# BFS 탐색
def bfs():
    while q:
        x, y = q.popleft()

        if x == m - 1 and y == n - 1:
            return True

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                push(new_x, new_y)
    return False

# 시작점 설정
push(0, 0)

# 탐색 후 결과 출력
if bfs():
    print(1)
else:
    print(0)