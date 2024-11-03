# 뱀이 없는 경우 : 1    / 뱀이 있는 경우 : 0
# 좌측 상단에서 출발하여, 우측 하단까지 뱀에게 물리지 않고 탈출할 경로가 있는가?
# 있으면 1  / 없으면 0
# 이동 가능 방향 : 아래, 오른쪽

# n행 m열
n, m = tuple(map(int, input().split()))
visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True

# 격자 정보 입력받기
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 격자 내부인지 여부 탐색
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 다음 격자로 이동할 수 있는지 여부 탐색
def can_go(x, y):
    # 1. 격자 범위 안에 있는가?
    if not in_range(x, y):
        return False
    
    # 2. 방문한 적 있거나, 뱀이 존재하는가?
    if visited[x][y] or grid[x][y] == 0:
        return False
    
    return True

# DFS 탐색
def dfs(x, y):
    # 목적지에 도달한 경우
    if x == n - 1 and y == m - 1:
        print(1)
        exit()

    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
            dfs(new_x, new_y)

dfs(0, 0)

print(0)