from collections import deque

# 입력 처리
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 거리 및 결과 격자 초기화
distances = [[-1] * n for _ in range(n)]
result = [[0] * n for _ in range(n)]
queue = deque()

# 비를 피할 수 있는 공간(3)에서 시작점 설정
for i in range(n):
    for j in range(n):
        if grid[i][j] == 3:
            queue.append((i, j))
            distances[i][j] = 0  # 시작점은 거리 0으로 설정

# BFS 수행
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 1 and distances[nx][ny] == -1:
            distances[nx][ny] = distances[x][y] + 1
            queue.append((nx, ny))

# 결과 처리
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:  # 사람이 있는 위치만 처리
            result[i][j] = distances[i][j] if distances[i][j] != -1 else -1

# 결과 출력
for row in result:
    print(*row)