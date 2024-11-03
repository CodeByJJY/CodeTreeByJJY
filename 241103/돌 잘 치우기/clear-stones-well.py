from collections import deque
from itertools import combinations

# 입력 처리
n, k, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

start_points = []
for _ in range(k):
    r, c = map(int, input().split())
    start_points.append((r - 1, c - 1))  # 0-index로 변환

# 모든 돌의 위치 찾기
stones = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]

# 방향 벡터 (상, 하, 좌, 우)
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 격자 내 여부 탐색
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# BFS 탐색
def bfs(grid, start_points):
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque(start_points)
    for x, y in start_points:
        visited[x][y] = True

    reachable_count = 0
    while q:
        x, y = q.popleft()
        reachable_count += 1

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if in_range(new_x, new_y) and not visited[new_x][new_y] and grid[new_x][new_y] == 0:
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

    return reachable_count

# 최댓값 계산
max_reachable = 0

# 돌 중 m개의 조합을 선택하여 탐색
for stones_to_remove in combinations(stones, m):
    # 격자 복사
    temp_grid = [row[:] for row in grid]

    # 돌 제거
    for x, y in stones_to_remove:
        temp_grid[x][y] = 0

    # BFS 실행
    reachable = bfs(temp_grid, start_points)
    max_reachable = max(max_reachable, reachable)

# 결과 출력
print(max_reachable)