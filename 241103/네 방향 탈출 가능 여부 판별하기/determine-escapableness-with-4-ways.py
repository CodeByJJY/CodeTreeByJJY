from collections import deque

# n행 m열
n, m = map(int, input().split())

# 격자 입력 받기 (0: 뱀 있음, 1: 뱀 없음)
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 방문 여부를 기록할 배열
visited = [[False for _ in range(m)] for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 격자 내 여부 탐색
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 이동 가능 여부 탐색
def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

# BFS 탐색
def bfs():
    q = deque()
    if grid[0][0] == 1:  # 시작점이 이동 가능하면 큐에 추가
        q.append((0, 0))
        visited[0][0] = True

    while q:
        x, y = q.popleft()

        # 도착 지점에 도달하면 탈출 가능
        if x == n - 1 and y == m - 1:
            return True

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

    # 도착 지점에 도달하지 못하면 탈출 불가능
    return False

# 탐색 후 결과 출력
if bfs():
    print(1)  # 탈출 가능한 경우
else:
    print(0)  # 탈출 불가능한 경우